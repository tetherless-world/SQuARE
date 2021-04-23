# SQuARE: the SPARQL Query Agent-based Reasoning Engine*
*This work is partially supported by IBM Research through the AI Horizons Network.

### Abstract
In order to support potential applications involving hybrid, distributed, or custom reasoning, as well as explainability in reasoning, we introduce SQuARE, the SPARQL Query Agent-based Reasoning Engine. SQuARE is a deductive inference engine implemented by encoding each OWL Description Logic (DL) axiom as a SPARQL CONSTRUCT query. We describe our approach for formulating the queries and implementing SQuARE within an existing knowledge management framework. While earlier work has proposed SPARQL extensions for various purposes, we find that the complete set of queries used in SPARQL-based reasoning methods are not publicly available. Our complete set of DL queries are made open-source along with our extensible test set, enabling reuse for novel applications in which similar approaches may be employed. SETS, the SQuARE Evaluation Test Set, includes example RDF representations for each DL axiom, enabling the testing of reasoning engines at a per axiom basis. Using SETS, we evaluate the DL complexity of existing reasoning engines. The approach described in this paper has benefits related to inference engine customization capabilities and of being able to reason over inconsistent knowledge.

# Table of Contents
- [SQuARE: the SPARQL Query Agent-based Reasoning Engine*](#square--the-sparql-query-agent-based-reasoning-engine-)
    + [Abstract](#abstract)
  * [Resources](#resources)
    + [Square Evaulation Test Set](#square-evaluation-test-set)
    + [SPARQL CONSTRUCT Axioms](#sparql-construct-axioms)
    + [Inclusion](#inclusion)
      - [Class Inclusion](#class-inclusion)
      - [Individual Inclusion](#individual-inclusion)
      - [Property Inclusion](#property-inclusion)
        * [Object Property Inclusion](#object-property-inclusion)
        * [Data Property Inclusion](#data-property-inclusion)
      - [Object Property Chain Inclusion](#object-property-chain-inclusion)
    + [Equivalence](#equivalence)
      - [Class Equivalence](#class-equivalence)
      - [Property Equivalence](#property-equivalence)
    + [Disjointness](#disjointness)
      - [Class Disjointness](#class-disjointness)
      - [Property Disjointness](#property-disjointness)
      - [All Disjoint Classes](#all-disjoint-classes)
      - [All Disjoint Properties](#all-disjoint-properties)
    + [Transitivity](#transitivity)
      - [Object Property Transitivity](#object-property-transitivity)
    + [Reflexivity](#reflexivity)
      - [Object Property Reflexivity](#object-property-reflexivity)
      - [Object Property Irreflexivity](#object-property-irreflexivity)
    + [Symmetry](#symmetry)
      - [Object Property Symmetry](#object-property-symmetry)
      - [Object Property Asymmetry](#object-property-asymmetry)
    + [Functionality](#functionality)
      - [Functional Object Property](#functional-object-property)
      - [Functional Data Property](#functional-data-property)
    + [Inversion](#inversion)
      - [Object Property Inversion](#object-property-inversion)
        * [Inverse Functional Object Property](#inverse-functional-object-property)
    + [Domain & Range Restrictions](#domain---range-restrictions)
      - [Property Domain](#property-domain)
      - [Property Range](#property-range)
    + [Datatype](#datatype)
      - [Datatype Restriction](#datatype-restriction)
    + [Assertions](#assertions)
      - [Same Individual](#same-individual)
      - [Different Individuals](#different-individuals)
      - [All Different Individuals](#all-different-individuals)
      - [Class Assertion](#class-assertion)
      - [Property Assertion](#property-assertion)
        * [Object Property Assertion](#object-property-assertion)
        * [Data Property Assertion](#data-property-assertion)
        * [Negative Object Property Assertion](#negative-object-property-assertion)
        * [Negative Data Property Assertion](#negative-data-property-assertion)
    + [Keys](#keys)
    + [Existential Quantification](#existential-quantification)
      - [Object Some Values From](#object-some-values-from)
      - [Data Some Values From](#data-some-values-from)
      - [Object Has Value](#object-has-value)
      - [Data Has Value](#data-has-value)
    + [Universal Quantification](#universal-quantification)
      - [Object All Values From](#object-all-values-from)
      - [Data All Values From](#data-all-values-from)
    + [Self Restriction](#self-restriction)
      - [Object Has Self](#object-has-self)
    + [Individual Enumeration](#individual-enumeration)
      - [Object One Of](#object-one-of)
        * [Object One Of Membership](#object-one-of-membership)
        * [Object One Of Inconsistency](#object-one-of-inconsistency)
      - [Data One Of](#data-one-of)
    + [Cardinality](#cardinality)
      - [Max Cardinality](#max-cardinality)
        * [Object Max Cardinality](#object-max-cardinality)
        * [Data Max Cardinality](#data-max-cardinality)
        * [Object Max Qualified Cardinality](#object-max-qualified-cardinality)
        * [Data Max Qualified Cardinality](#data-max-qualified-cardinality)
      - [Min Cardinality](#min-cardinality)
        * [Object Min Cardinality](#object-min-cardinality)
        * [Data Min Cardinality](#data-min-cardinality)
        * [Object Min Qualified Cardinality](#object-min-qualified-cardinality)
        * [Data Min Qualified Cardinality](#data-min-qualified-cardinality)
      - [Exact Cardinality](#exact-cardinality)
        * [Object Exact Cardinality](#object-exact-cardinality)
        * [Data Exact Cardinality](#data-exact-cardinality)
        * [Object Exact Qualified Cardinality](#object-exact-qualified-cardinality)
        * [Data Exact Qualified Cardinality](#data-exact-qualified-cardinality)
    + [Disjunction](#disjunction)
      - [Object Union Of](#object-union-of)
      - [Data Union Of](#data-union-of)
      - [Disjoint Union](#disjoint-union)
    + [Intersection](#intersection)
      - [Object Intersection Of](#object-intersection-of)
      - [Data Intersection Of](#data-intersection-of)
    + [Negation](#negation)
      - [Complement Of](#complement-of)
        * [Object Complement Of](#object-complement-of)
        * [Data Complement Of](#data-complement-of)
        * [Object Property Complement Of](#object-property-complement-of)
        * [Data Property Complement Of](#data-property-complement-of)
    + [Code](#code)
      - [Deductor Agent](#deductor-agent)
      - [Backtracer Agent](#backtracer-agent)
    + [Support or Contact](#support-or-contact)

## Resources

### Square Evaluation Test Set
The documentation for the test set is available [here](documentation.html).

The consistent version of the test set is available [here](https://raw.githubusercontent.com/tetherless-world/validation/main/valo.ttl).

The inconsistent version of the test set is available [here](https://raw.githubusercontent.com/tetherless-world/validation/main/valo_inconsistent.ttl).

### SPARQL CONSTRUCT Axioms
### Inclusion 
#### Class Inclusion
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=C_1%20\sqsubseteq%20C_2)

**Query**

```
CONSTRUCT {
  ?resource rdfs:subClassOf ?superClass .
}
WHERE {
  ?resource rdfs:subClassOf ?class .
  ?class rdfs:subClassOf+ ?superClass .
}
```

**Explanation**

Since _class_ is a subclass of _superClass_, any class that is a subclass of _class_ is also a subclass of _superClass_. Therefore, _resource_ is a subclass of _superClass_.

**Example**

```
sio:Entity rdf:type owl:Class ;
    rdfs:label "entity" ;
    dct:description "Every thing is an entity." .

sio:Object rdf:type owl:Class ;
    rdfs:subClassOf sio:Entity ;
    rdfs:label "object" ;
    dct:description "An object is an entity that is wholly identifiable at any instant of time during which it exists." .

sio:MaterialEntity  rdf:type owl:Class ;
    rdfs:label "material entity" ;
    rdfs:subClassOf sio:Object ;
    dct:description "A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass." .
```
A reasoner should infer `sio:MaterialEntity rdfs:subClassOf sio:Entity .` 
#### Individual Inclusion
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=a:C)

**Query**

```
CONSTRUCT {
  ?resource rdf:type ?superClass .
}
WHERE {
  ?resource rdf:type ?class .
  ?class rdfs:subClassOf+ ?superClass .
}
```
**Explanation**

Any instance of _class_ is also an instance of _superClass_. Therefore, since _resource_ is a _class_, it also is a _superClass_.

**Example**

```
sio:Role rdf:type owl:Class ;
    rdfs:label "role" ;
    rdfs:subClassOf sio:RealizableEntity ;
    dct:description "A role is a realizable entity that describes behaviours, rights and obligations of an entity in some particular circumstance." .

val-kb:Farmer rdf:type sio:Role ;
    rdfs:label "farmer" .
```
A reasoner should infer `val-kb:Farmer rdf:type sio:RealizableEntity .`
#### Property Inclusion
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=P_1%20\sqsubseteq%20P_2)

**Query**
```
CONSTRUCT {
  ?resource ?superProperty ?o .
}
WHERE {
  ?resource ?p ?o .
  ?p rdf:type owl:Property ;
    rdfs:subPropertyOf+ ?superProperty .
}
```
**Explanation**

Any subject and object related by the property _p_ is also related by _superProperty_. Therefore, since _resource_ _p_ _o_, it is implied that _resource_ _superProperty_ _o_.

**Example**

```
```
A reasoner should infer ` `
##### Object Property Inclusion

**Query**

```
CONSTRUCT {
  ?resource ?superProperty ?o .
}
WHERE {
  ?resource ?p ?o .
  ?p rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf+ ?superProperty .
}
```
**Explanation**

Any subject and object related by the property _p_ is also related by _superProperty_. Therefore, since _resource_ _p_ _o_, it is implied that _resource_ _superProperty_ _o_.

**Example**

```
sio:Age rdf:type owl:Class ;
    rdfs:label "age" ;
    rdfs:subClassOf sio:DimensionalQuantity ;
    dct:description "Age is the length of time that a person has lived or a thing has existed." .

sio:DimensionlessQuantity rdf:type owl:Class ;
    rdfs:label "dimensionless quantity" ;
    rdfs:subClassOf sio:Quantity ,
        [ rdf:type owl:Class ;
            owl:complementOf [ rdf:type owl:Restriction ;
                owl:onProperty sio:hasUnit ;
                owl:someValuesFrom sio:UnitOfMeasurement ] ];
    owl:disjointWith sio:DimensionalQuantity ;
    dct:description "A dimensionless quantity is a quantity that has no associated unit." .

sio:Quantity rdf:type owl:Class ;
    rdfs:label "quantity" ;
    owl:equivalentClass 
        [ rdf:type owl:Class ; 
            owl:unionOf (sio:DimensionlessQuantity sio:DimensionalQuantity) ] ;
    rdfs:subClassOf sio:MeasurementValue ;
    dct:description "A quantity is an informational entity that gives the magnitude of a property." .

sio:MeasurementValue rdf:type owl:Class ;
    rdfs:label "measurement value" ;
    rdfs:subClassOf sio:Number ;
    dct:description "A measurement value is a quantitative description that reflects the magnitude of some attribute." .

sio:Number rdf:type owl:Class ;
    rdfs:label "number" ;
    rdfs:subClassOf sio:MathematicalEntity ;
    dct:description "A number is a mathematical object used to count, label, and measure." .

val-kb:Samantha sio:hasProperty val-kb:AgeOfSamantha .

val-kb:AgeOfSamantha rdf:type sio:Age ;
    rdfs:label "Samantha's age" .
```
A reasoner should infer `val-kb:Samantha sio:hasAttribute val-kb:AgeOfSamantha .`
##### Data Property Inclusion

**Query**

```
CONSTRUCT {
  ?resource ?superProperty ?o .
}
WHERE {
  ?resource ?p ?o .
  ?p rdf:type owl:DatatypeProperty ;
    rdfs:subPropertyOf+ ?superProperty .
}
```
**Explanation**

Any subject and object related by the property _p_ is also related by _superProperty_. Therefore, since _resource_ _p_ _o_, it is implied that _resource_ _superProperty_ _o_.

**Example**

```
valo:hasExactValue rdf:type owl:DatatypeProperty ;
    rdfs:label "has exact value" ;
    rdfs:subPropertyOf sio:hasValue .

val-kb:AgeOfSamantha valo:hasExactValue "25.82"^^xsd:decimal .
```
A reasoner should infer `val-kb:AgeOfSamantha sio:hasValue 25.82 .`
#### Object Property Chain Inclusion

**Query**

```
CONSTRUCT {
  ?resource ?objectProperty ?o .
}
WHERE {
  ?objectProperty rdf:type owl:ObjectProperty ;
    owl:propertyChainAxiom ?list .
  ?list rdf:first ?prop1 .
  ?list rdf:rest/rdf:first ?prop2 .
  ?resource ?prop1 [ ?prop2 ?o ] .
}
```
**Explanation**

**Example**
```
sio:isLocatedIn rdf:type owl:ObjectProperty ,
                                owl:TransitiveProperty ;
    rdfs:subPropertyOf sio:isSpatiotemporallyRelatedTo ;
    rdfs:label "is located in" ;
    dct:description "A is located in B iff the spatial region occupied by A is part of the spatial region occupied by B." .

sio:isPartOf rdf:type owl:ObjectProperty ,
                                owl:TransitiveProperty ,
                                owl:ReflexiveProperty ;
    rdfs:subPropertyOf sio:isLocatedIn ;
    rdfs:label "is part of" ;
    dct:description "is part of is a transitive, reflexive and anti-symmetric mereological relation between a whole and itself or a part and its whole." .
    
sio:isRelatedTo rdf:type owl:ObjectProperty ,
                                owl:SymmetricProperty ;
    rdfs:label "is related to" ;
    dct:description "A is related to B iff there is some relation between A and B." .

sio:isSpatiotemporallyRelatedTo rdf:type owl:ObjectProperty ,
                                owl:SymmetricProperty ;
    rdfs:subPropertyOf sio:isRelatedTo ;
    rdfs:label "is spatiotemporally related to" ;
    dct:description "A is spatiotemporally related to B iff A is in the spatial or temporal vicinity of B" .

sio:overlapsWith rdf:type owl:ObjectProperty ,
        owl:SymmetricProperty ,
        owl:ReflexiveProperty ;
    rdfs:subPropertyOf sio:isSpatiotemporallyRelatedTo ;
    owl:propertyChainAxiom ( sio:overlapsWith sio:isPartOf ) ;
    dct:description "A overlaps with B iff there is some C that is part of both A and B." ;
    rdfs:label "overlaps with" .

val-kb:Rug rdf:type sio:Object ;
    rdfs:label "rug" ;
    sio:overlapsWith ex-kb:FloorPanel .

val-kb:FloorPanel rdf:type sio:Object ;
    rdfs:label "floor panel" ;
    sio:isPartOf ex-kb:Floor .

val-kb:Floor rdf:type sio:Object ;
    rdfs:label "floor" .
```
A reasoner should infer `val-kb:Rug sio:overlapsWith val-kb:Floor .`
### Equivalence
#### Class Equivalence
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=C_1\equiv%20C_2)

**Query**
```
CONSTRUCT {
  ?resource rdf:type ?equivClass .
}
WHERE {
  ?resource rdf:type ?superClass.
  {?superClass owl:equivalentClass ?equivClass .}
    UNION
  {?equivClass owl:equivalentClass ?superClass .}
}

```
**Explanation**

_superClass_ is equivalent to _equivClass_, so since _resource_ is a _superClass_, it is also a _equivClass_.

**Example**
```
valo:Fake rdf:type owl:Class ;
    owl:equivalentClass sio:Fictional ;
    rdfs:label "fake" .

val-kb:Hubert rdf:type valo:Fake ;
    rdfs:label "Hubert" .
```
A reasoner should infer `{val-kb:Hubert rdf:type sio:Fictional .`
#### Property Equivalence
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=P_1\equiv%20P_2)

**Query**
```
CONSTRUCT {
  ?resource ?equivProperty ?o .
}
WHERE {
  ?resource ?p ?o .
  {?p owl:equivalentProperty ?equivProperty .}
    UNION
  {?equivProperty owl:equivalentProperty ?p . }
}
```
**Explanation**

The properties _p_ and _equivProperty_ are equivalent. Therefore, since _resource_ _p_ _o_, it is implied that _resource_ _equivProperty_ _o_.

**Example**
```
sio:hasValue rdf:type owl:DatatypeProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has value" ;
    dct:description "A relation between a informational entity and its actual value (numeric, date, text, etc)." .

val-kb:AgeOfSamantha rdf:type sio:Age ;
    rdfs:label "Samantha's age" ;
    sio:hasValue "25.82"^^xsd:decimal .

valo:hasValue rdf:type owl:DatatypeProperty ;
    rdfs:label "has value" ;
    owl:equivalentProperty sio:hasValue .
```
A reasoner should infer `val-kb:AgeOfSamantha valo:hasValue 25.82 .`
### Disjointness
#### Class Disjointness
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=C_1\neq%20C_2)

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class .
  ?resource rdf:type ?disjointClass .
  { ?class owl:disjointWith ?disjointClass . } 
    UNION
  { ?disjointClass owl:disjointWith ?class . }
}
```
**Explanation**

Since _class_ is a disjoint with _disjointClass_, any resource that is an instance of _class_ is not an instance of _disjointClass_. Therefore, since _resource_ is an instance of _class_, it can not be an instance of _disjointClass_.

**Example**
```
sio:Entity rdf:type owl:Class ;
    rdfs:label "entity" ;
    dct:description "Every thing is an entity." .

sio:Attribute rdf:type owl:Class ;
    rdfs:subClassOf sio:Entity ;
    rdfs:label "attribute" ;
    dct:description "An attribute is a characteristic of some entity." .

sio:RealizableEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Attribute ;
    dct:description "A realizable entity is an attribute that is exhibited under some condition and is realized in some process." ;
    rdfs:label "realizable entity" .

sio:Quality rdf:type owl:Class ;
    rdfs:subClassOf sio:Attribute ;
    owl:disjointWith sio:RealizableEntity ;
    dct:description "A quality is an attribute that is intrinsically associated with its bearer (or its parts), but whose presence/absence and observed/measured value may vary." ;
    rdfs:label "quality" .

sio:ExistenceQuality rdf:type owl:Class ;
    rdfs:subClassOf sio:Quality ;
    dct:description "existence quality is the quality of an entity that describe in what environment it is known to exist." ;
    rdfs:label "existence quality" .

sio:Virtual rdf:type owl:Class ;
    rdfs:subClassOf sio:ExistenceQuality ;
    dct:description "virtual is the quality of an entity that exists only in a virtual setting such as a simulation or game environment." ;
    rdfs:label "virtual" .

sio:Real rdf:type owl:Class ;
    rdfs:subClassOf sio:ExistenceQuality ;
    owl:disjointWith sio:Fictional ;
    owl:disjointWith sio:Virtual ;
    dct:description "real is the quality of an entity that exists in real space and time." ;
    rdfs:label "real" .

sio:Hypothetical rdf:type owl:Class ;
    rdfs:subClassOf sio:ExistenceQuality ;
    dct:description "hypothetical is the quality of an entity that is conjectured to exist." ;
    rdfs:label "hypothetical" .

sio:Fictional rdf:type owl:Class ;
    rdfs:subClassOf sio:Hypothetical ;
    dct:description "fictional is the quality of an entity that exists only in a creative work of fiction." ;
    rdfs:label "fictional" .

val-kb:ImaginaryFriend
    rdfs:label "my imaginary friend" ;
    rdf:type sio:Real ;
    rdf:type sio:Fictional .
```
A reasoner should infer `val-kb:ImaginaryFriend rdf:type owl:Nothing .` or that an inconsistency occurs.
#### Property Disjointness
**Axiom**


**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?p1 ?o1 ,
      ?o2 .
  ?resource ?p2 ?o2.
  {?p1 owl:propertyDisjointWith ?p2 .}
    UNION
  {?p2 owl:propertyDisjointWith ?p1 .}
}
```
**Explanation**

Since properties _p1_ and _p2_ are disjoint, _resource_ having both _p2_ _o2_ as well as _p1_ _o2_ leads to an inconsistency.

**Example**
```
valo:hasMother rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf sio:hasAttribute ;
    rdfs:label "has mother" ;
    owl:propertyDisjointWith valo:hasFather .

valo:hasFather rdf:type owl:ObjectProperty ;
    rdfs:label "has father" .

val-kb:Jordan rdf:type sio:Human ;
    rdfs:label "Jordan" .

val-kb:Susan rdf:type sio:Human ;
    rdfs:label "Susan" ;
    valo:hasFather val-kb:Jordan ;
    valo:hasMother val-kb:Jordan .
```
A reasoner should infer `val-kb:Susan rdf:type owl:Nothing .` or that an inconsistency occurs.
#### All Disjoint Classes
**Axiom**


**Query**
```
CONSTRUCT {
  ?member owl:disjointWith ?item .
}
WHERE {
  ?restriction rdf:type owl:AllDisjointClasses ;
    owl:members ?list .
  ?list rdf:rest*/rdf:first ?member .
  {
    SELECT DISTINCT ?item ?restrict WHERE
    {
      ?restrict rdf:type owl:AllDisjointClasses ;
        owl:members ?list .
      ?list rdf:rest*/rdf:first ?item .
    }
  }
  BIND(?restriction AS ?restrict)
  FILTER(?member != ?item)
}
```
**Explanation**

Since _restriction_ is an all disjoint classes restriction with classes listed in _list_, each member in _list_ is disjoint with each other member in the list.

**Example**
```
sio:Entity rdf:type owl:Class ;
    rdfs:label "entity" ;
    dct:description "Every thing is an entity." .

sio:Process rdf:type owl:Class ;
    rdfs:subClassOf sio:Entity ;
    dct:description "A process is an entity that is identifiable only through the unfolding of time, has temporal parts, and unless otherwise specified/predicted, cannot be identified from any instant of time in which it exists." ;
    rdfs:label "process" .

sio:Attribute rdf:type owl:Class ;
    rdfs:subClassOf sio:Entity ;
    rdfs:label "attribute" ;
    dct:description "An attribute is a characteristic of some entity." .

sio:Object rdf:type owl:Class ;
    rdfs:subClassOf sio:Entity ;
    rdfs:label "object" ;
    dct:description "An object is an entity that is wholly identifiable at any instant of time during which it exists." .

[ rdf:type owl:AllDisjointClasses ;
    owl:members ( sio:Process sio:Attribute sio:Object ) ] .
```
A reasoner should infer `sio:Process owl:disjointWith sio:Object , sio:Attribute . sio:Attribute owl:disjointWith sio:Object , sio:Process . sio:Object owl:disjointWith sio:Attribute, sio:Process .`
#### All Disjoint Properties
**Axiom**

**Query**
```
CONSTRUCT {
  ?member owl:propertyDisjointWith ?item .
}
WHERE {
  ?restriction rdf:type owl:AllDisjointProperties ;
    owl:members ?list .
  ?list rdf:rest*/rdf:first ?member .
  {
    SELECT DISTINCT ?item ?restrict WHERE
    {
      ?restrict rdf:type owl:AllDisjointProperties ;
        owl:members ?list .
      ?list rdf:rest*/rdf:first ?item .
    }
  }
  BIND(?restriction AS ?restrict)
  FILTER(?member != ?item)
}
```
**Explanation**

Since _restriction_ is an all disjoint properties restriction with properties listed in _list_, each member in _list_ is disjoint with each other property in the list.

**Example**
```
val-kb:DisjointPropertiesRestriction rdf:type owl:AllDisjointProperties ;
    owl:members ( valo:hasMother valo:hasFather valo:hasSibling ) .

valo:hasMother rdf:type owl:ObjectProperty ;
    rdfs:label "has mother" .

valo:hasFather rdf:type owl:ObjectProperty ;
    rdfs:label "has father" .

valo:hasSibling rdf:type owl:ObjectProperty ;
    rdfs:label "has sibling" .
```
A reasoner should infer `valo:hasMother owl:propertyDisjointWith valo:hasFather , valo:hasSibling . valo:hasFather owl:propertyDisjointWith valo:hasMother , valo:hasSibling . valo:hasSibling owl:propertyDisjointWith valo:hasMother , valo:hasFather .`
### Transitivity
#### Object Property Transitivity
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=P^+%20\sqsubseteq%20P)

**Query**
```
CONSTRUCT {
  ?resource ?transitiveProperty ?o2 .
}
WHERE {
  ?resource ?transitiveProperty ?o1 .
  ?o1 ?transitiveProperty ?o2 .
  ?transitiveProperty rdf:type owl:TransitiveProperty .
}
```
**Explanation**

Since _transitiveProperty_ is a transitive object property, and the relationships _resource_ _transitiveProperty_ _o1_ and _o1_ _transitiveProperty_ _o2_ exist, then we can infer that _resource_ _transitiveProperty_ _o2_.

**Example**
```
sio:isRelatedTo rdf:type owl:ObjectProperty ,
                                owl:SymmetricProperty ;
    rdfs:label "is related to" ;
    dct:description "A is related to B iff there is some relation between A and B." .

sio:isSpatiotemporallyRelatedTo rdf:type owl:ObjectProperty ,
                                owl:SymmetricProperty ;
    rdfs:subPropertyOf sio:isRelatedTo ;
    rdfs:label "is spatiotemporally related to" ;
    dct:description "A is spatiotemporally related to B iff A is in the spatial or temporal vicinity of B" .

sio:isLocationOf rdf:type owl:ObjectProperty ,
                                owl:TransitiveProperty ;
    rdfs:subPropertyOf sio:isSpatiotemporallyRelatedTo ;
    rdfs:label "is location of" ;
    dct:description "A is location of B iff the spatial region occupied by A has the spatial region occupied by B as a part." .

sio:hasPart rdf:type owl:ObjectProperty ,
                                owl:TransitiveProperty ,
                                owl:ReflexiveProperty ;
    rdfs:subPropertyOf sio:isLocationOf ;
    owl:inverseOf sio:isPartOf ;
    rdfs:label "has part" ;
    dct:description "has part is a transitive, reflexive and antisymmetric relation between a whole and itself or a whole and its part" .

sio:isLocatedIn rdf:type owl:ObjectProperty ,
                                owl:TransitiveProperty ;
    rdfs:subPropertyOf sio:isSpatiotemporallyRelatedTo ;
    rdfs:label "is located in" ;
    dct:description "A is located in B iff the spatial region occupied by A is part of the spatial region occupied by B." .

sio:isPartOf rdf:type owl:ObjectProperty ,
                                owl:TransitiveProperty ,
                                owl:ReflexiveProperty ;
    rdfs:subPropertyOf sio:isLocatedIn ;
    rdfs:label "is part of" ;
    dct:description "is part of is a transitive, reflexive and anti-symmetric mereological relation between a whole and itself or a part and its whole." .

val-kb:Fingernail rdf:type owl:Individual ;
    rdfs:label "finger nail" ;
    sio:isPartOf val-kb:Finger .

val-kb:Finger rdf:type owl:Individual ;
    rdfs:label "finger" ;
    sio:isPartOf val-kb:Hand . 

val-kb:Hand rdf:type owl:Individual ;
    rdfs:label "hand" .
```
A reasoner should infer `val-kb:Fingernail sio:isPartOf val-kb:Hand .`
### Reflexivity
#### Object Property Reflexivity
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource ?reflexiveProperty ?resource .
}
WHERE {
  ?resource rdf:type ?type ;
    ?reflexiveProperty ?o .
  ?o rdf:type ?type.
  ?reflexiveProperty rdf:type owl:ReflexiveProperty .
}
```
**Explanation**

Since _resource_ has a _reflexiveProperty_ assertion to _o_, _resource_ and _o_ are both of type _type_, and _reflexiveProperty_ is a reflexive property, we can infer that _resource_ _reflexiveProperty_ _resource_.

**Example**
```
sio:Process rdf:type owl:Class ;
    rdfs:subClassOf sio:Entity ;
    dct:description "A process is an entity that is identifiable only through the unfolding of time, has temporal parts, and unless otherwise specified/predicted, cannot be identified from any instant of time in which it exists." ;
    rdfs:label "process" .

val-kb:Workflow rdf:type sio:Process ;
    rdfs:label "workflow" ;
    sio:hasPart val-kb:Step .

val-kb:Step rdf:type sio:Process ;
    rdfs:label "step" .
```
A reasoner should infer `val-kb:Workflow sio:hasPart val-kb:Workflow .`
#### Object Property Irreflexivity
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?irreflexiveProperty ?o .
  ?irreflexiveProperty rdf:type owl:IrreflexiveProperty .
  ?resource ?irreflexiveProperty ?resource .
}
```
**Explanation**

Since _resource_ has a _irreflexiveProperty_ assertion, and _irreflexiveProperty_ is a irreflexive property, we can infer that the relationship _resource_ _irreflexiveProperty_ _resource_ does not exist.

**Example**
```
sio:hasMember rdf:type owl:ObjectProperty ,
                                owl:IrreflexiveProperty ;
    rdfs:subPropertyOf sio:hasAttribute ;
    owl:inverseOf sio:isMemberOf ;
    rdfs:label "has member" ;
    dct:description "has member is a mereological relation between a collection and an item." .

sio:isMemberOf rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf sio:isAttributeOf ;
    rdfs:label "is member of" ;
    dct:description "is member of is a mereological relation between a item and a collection." .

sio:Collection rdf:type owl:Class ;
    rdfs:subClassOf sio:Set ;
    rdfs:label "collection" ;
    dct:description "A collection is a set for which there exists at least one member, although any member need not to exist at any point in the collection's existence." .

sio:Set rdf:type owl:Class ;
    rdfs:subClassOf sio:MathematicalEntity ;
    rdfs:label "set" ;
    dct:description "A set is a collection of entities, for which there may be zero members." .

sio:MathematicalEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:InformationContentEntity ;
    rdfs:label "mathematical entity" ;
    dct:description "A mathematical entity is an information content entity that are components of a mathematical system or can be defined in mathematical terms." .

sio:InformationContentEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Object ;
    rdfs:label "information content entity" ;
    dct:description "An information content entity is an object that requires some background knowledge or procedure to correctly interpret." .

val-kb:Group rdf:type sio:Collection ;
    rdfs:label "group" ;
    sio:hasMember val-kb:Group .
```
A reasoner should infer `val-kb:Group rdf:type owl:Nothing .` or that an inconsistency occurs.
### Symmetry
#### Object Property Symmetry
**Axiom**
![formula](https://render.githubusercontent.com/render/math?math=R\sqsubseteq%20R^-)
**Query**
```
CONSTRUCT {
  ?o ?symmetricProperty ?resource .
}
WHERE {
  ?resource ?symmetricProperty ?o .
  ?symmetricProperty rdf:type owl:SymmetricProperty .
}
```
**Explanation**

Since _symmetricProperty_ is a symmetric property, and _resource_ _symmetricProperty_ _o_, we can infer that _o_ _symmetricProperty_ _resource_.

**Example**
```
sio:isRelatedTo rdf:type owl:ObjectProperty ,
                                owl:SymmetricProperty ;
    rdfs:label "is related to" ;
    dct:description "A is related to B iff there is some relation between A and B." .

val-kb:Peter rdf:type sio:Human ;
    rdfs:label "Peter" ;
    sio:isRelatedTo val-kb:Samantha .

val-kb:Samantha rdf:type sio:Human ;
    rdfs:label "Samantha" .
```
A reasoner should infer `val-kb:Samantha sio:isRelatedTo val-kb:Peter .`
#### Object Property Asymmetry
**Axiom**
![formula](https://render.githubusercontent.com/render/math?math=R\sqsubseteq%20\neg%20R^-)
**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?asymmetricProperty ?o .
  ?asymmetricProperty rdf:type owl:AsymmetricProperty .
  ?o ?asymmetricProperty ?resource .
}
```
**Explanation**

Since _asymmetricProperty_ is an asymmetric property, and _resource_ _asymmetricProperty_ _o_, then the assertion _o_ _asymmetricProperty_ _resource_ results in an inconsistency.

**Example**
```
sio:isProperPartOf rdf:type owl:ObjectProperty ,
                                owl:AsymmetricProperty ,
                                owl:IrreflexiveProperty ;
    rdfs:label "is proper part of" ;
    rdfs:subPropertyOf sio:isPartOf ;
    dct:description "is proper part of is an asymmetric, irreflexive (normally transitive) relation between a part and its distinct whole." .

val-kb:Nose rdf:type owl:Individual ;
    rdfs:label "nose" ;
    sio:isProperPartOf val-kb:Face .

val-kb:Face rdf:type owl:Individual ;
    sio:isProperPartOf val-kb:Nose ;
    rdfs:label "face" .
```
A reasoner should infer `val-kb:Face rdf:type owl:Nothing .` , `val-kb:Nose rdf:type owl:Nothing .` , and/or that an inconsistency occurs.
### Functionality
**Axiom**
![formula](https://render.githubusercontent.com/render/math?math=\text{T}%20\sqsubseteq%20\leq%201%20R.\text{T})
#### Functional Object Property

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?functionalProperty ?o1 ,
      ?o2 .
  ?functionalProperty rdf:type owl:ObjectProperty , 
      owl:FunctionalProperty .
  FILTER (str(?o1) !=  str(?o2))
}
```
**Explanation**

Since _functionalProperty_ is a functional object property, _resource_ can only have one value for _functionalProperty_. Since _resource_ _functionalProperty_ both _o1_ and _o2_, we can infer that _o1_ and _o2_ must be the same individual.

**Example**
```
sio:Role rdf:type owl:Class ;
    rdfs:label "role" ;
    rdfs:subClassOf sio:RealizableEntity ;
    dct:description "A role is a realizable entity that describes behaviours, rights and obligations of an entity in some particular circumstance." .

sio:isAttributeOf rdf:type owl:ObjectProperty ;
    rdfs:label "is attribute of" ;
    dct:description "is attribute of is a relation that associates an attribute with an entity where an attribute is an intrinsic characteristic such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier) either directly or indirectly through generalization of entities of the same type." ;
    rdfs:subPropertyOf sio:isRelatedTo .

sio:hasAttribute rdf:type owl:ObjectProperty ;
    rdfs:label "has attribute" ;
    dct:description "has attribute is a relation that associates a entity with an attribute where an attribute is an intrinsic characteristic such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier) either directly or indirectly through generalization of entities of the same type." ;
    rdfs:subPropertyOf sio:isRelatedTo .

sio:isPropertyOf rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "is property of" ;
    dct:description "is property of is a relation betweena  quality, capability or role and the entity that it and it alone bears." ;
    rdfs:subPropertyOf sio:isAttributeOf .

sio:hasProperty rdf:type owl:ObjectProperty ,
                                owl:InverseFunctionalProperty;
    rdfs:label "has property" ;
    owl:inverseOf sio:isPropertyOf ;
    dct:description "has property is a relation between an entity and the quality, capability or role that it and it alone bears." ;
    rdfs:subPropertyOf sio:hasAttribute .

sio:hasRealizableProperty rdf:type owl:ObjectProperty ,
                                owl:InverseFunctionalProperty;
    rdfs:label "has realizable property" ;
    rdfs:subPropertyOf sio:hasProperty .

sio:isRealizablePropertyOf rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "is realizable property of" ;
    rdfs:subPropertyOf sio:isPropertyOf ;
    owl:inverseOf sio:hasRealizableProperty .

sio:isRoleOf rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "is role of" ;
    rdfs:domain sio:Role ;
    rdfs:subPropertyOf sio:isRealizablePropertyOf ;
    dct:description "is role of is a relation between a role and the entity that it is a property of." ;
    owl:inverseOf sio:hasRole .
    
val-kb:Tutor rdf:type sio:Human ;
    rdfs:label "tutor" .

val-kb:TeachingRole rdf:type sio:Role ;
    rdfs:label "teaching role" ;
    sio:isRoleOf val-kb:Tutor .

val-kb:TutoringRole rdf:type sio:Role ;
    rdfs:label "tutoring role" ;
    sio:isRoleOf val-kb:Tutor .
```
A reasoner should infer `val-kb:TeachingRole owl:sameAs val-kb:TutoringRole .`
#### Functional Data Property
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?functionalProperty ?o1 , 
      ?o2 .
  ?functionalProperty rdf:type owl:DatatypeProperty , 
      owl:FunctionalProperty .
  FILTER (str(?o1) !=  str(?o2))
}
```
**Explanation**

Since _functionalProperty_ is a functional data property, _resource_ can only have one value for _functionalProperty_. Since _resource_ _functionalProperty_ both _o1_ and _o2_, and _o1_ is different from _o2_, an inconsistency occurs.

**Example**
```
sio:hasValue rdf:type owl:DatatypeProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has value" ;
    dct:description "A relation between a informational entity and its actual value (numeric, date, text, etc)." .

val-kb:HeightOfTom sio:hasValue "5"^^xsd:integer .
val-kb:HeightOfTom sio:hasValue "6"^^xsd:integer .
```
A reasoner should infer `val-kb:HeightOfTom rdf:type owl:Nothing .` or that an inconsistency occurs.
### Inversion
#### Object Property Inversion
**Axiom**

**Query**
```
CONSTRUCT {
  ?o ?inverseProperty ?resource .
}
WHERE {
  ?resource ?p ?o .
  ?p rdf:type owl:ObjectProperty .
  {?p owl:inverseOf ?inverseProperty .}
    UNION
  {?inverseProperty owl:inverseOf ?p . }
}
```
**Explanation**

The object properties _p_ and _inverseProperty_ are inversely related to eachother. Therefore, since _resource_ _p_ _o_, it is implied that _o_ _inverseProperty_ _resource_.

**Example**
```
sio:hasAttribute rdf:type owl:ObjectProperty ;
    rdfs:label "has attribute" ;
    dct:description "has attribute is a relation that associates a entity with an attribute where an attribute is an intrinsic characteristic such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier) either directly or indirectly through generalization of entities of the same type." ;
    rdfs:subPropertyOf sio:isRelatedTo .

sio:hasProperty rdf:type owl:ObjectProperty ,
                                owl:InverseFunctionalProperty;
    rdfs:label "has property" ;
    owl:inverseOf sio:isPropertyOf ;
    dct:description "has property is a relation between an entity and the quality, capability or role that it and it alone bears." ;
    rdfs:subPropertyOf sio:hasAttribute .

sio:Symbol rdf:type owl:Class ;
    rdfs:subClassOf sio:Representation ;
    dct:description "A symbol is a proposition about what an entity represents." ;
    rdfs:label "symbol" .

sio:InformationContentEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Object ;
    rdfs:label "information content entity" ;
    dct:description "An information content entity is an object that requires some background knowledge or procedure to correctly interpret." .

sio:Representation rdf:type owl:Class ;
    rdfs:subClassOf sio:InformationContentEntity ;
    dct:description "A representation is a entity that in some way represents another entity (or attribute thereof)." ;
    rdfs:label "representation" .

valo:MolecularFormula rdfs:subClassOf sio:Symbol ;
    rdfs:label "molecular formula" .

val-kb:Water sio:hasAttribute val-kb:H2O ;
    rdfs:label "water" .

val-kb:HyrdogenDioxide sio:hasAttribute val-kb:H2O ;
    rdfs:label "hydrogen dioxide" .

val-kb:H2O rdf:type valo:MolecularFormula ;
    rdfs:label "H2O" .
```
A reasoner should infer `val-kb:Water owl:sameAs val-kb:HyrdogenDioxide .`
##### Inverse Functional Object Property
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource owl:sameAs ?individual .
}
WHERE {
  ?resource ?invFunctionalProperty ?o .
  ?individual ?invFunctionalProperty ?o .
  ?invFunctionalProperty rdf:type owl:ObjectProperty ,
      owl:InverseFunctionalProperty .
}
```
**Explanation**

Since _invFunctionalProperty_ is an inverse functional property, and _resource_ and _individual_ both have the relationship _invFunctionalProperty_ _o_, then we can infer that _resource_ is the same as _individual_.

**Example**

```
sio:hasAttribute rdf:type owl:ObjectProperty ;
    rdfs:label "has attribute" ;
    dct:description "has attribute is a relation that associates a entity with an attribute where an attribute is an intrinsic characteristic such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier) either directly or indirectly through generalization of entities of the same type." ;
    rdfs:subPropertyOf sio:isRelatedTo .

sio:hasProperty rdf:type owl:ObjectProperty ,
                                owl:InverseFunctionalProperty;
    rdfs:label "has property" ;
    owl:inverseOf sio:isPropertyOf ;
    dct:description "has property is a relation between an entity and the quality, capability or role that it and it alone bears." ;
    rdfs:subPropertyOf sio:hasAttribute .

sio:Entity rdf:type owl:Class ;
    rdfs:label "entity" ;
    dct:description "Every thing is an entity." .

sio:Object rdf:type owl:Class ;
    rdfs:subClassOf sio:Entity ;
    rdfs:label "object" ;
    dct:description "An object is an entity that is wholly identifiable at any instant of time during which it exists." .

sio:InformationContentEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Object ;
    rdfs:label "information content entity" ;
    dct:description "An information content entity is an object that requires some background knowledge or procedure to correctly interpret." .

sio:Representation rdf:type owl:Class ;
    rdfs:subClassOf sio:InformationContentEntity ;
    dct:description "A representation is a entity that in some way represents another entity (or attribute thereof)." ;
    rdfs:label "representation" .

sio:Symbol rdf:type owl:Class ;
    rdfs:subClassOf sio:Representation ;
    dct:description "A symbol is a proposition about what an entity represents." ;
    rdfs:label "symbol" .

valo:MolecularFormula rdfs:subClassOf sio:Symbol ;
    rdfs:label "molecular formula" .

val-kb:Water sio:hasProperty ex-kb:H2O ;
    rdfs:label "water" .

val-kb:HyrdogenDioxide sio:hasProperty ex-kb:H2O ;
    rdfs:label "hydrogen dioxide" .

val-kb:H2O rdf:type ex:MolecularFormula ;
    rdfs:label "H2O" .
```
A reasoner should infer `val-kb:Water owl:sameAs val-kb:HyrdogenDioxide .`
### Domain & Range Restrictions
#### Property Domain
**Axiom**
![formula](https://render.githubusercontent.com/render/math?math=\exists%20R.\text{T}%20\sqsubseteq%20C)
**Query**
```
CONSTRUCT {
  ?resource rdf:type ?class .
}
WHERE {
  ?resource ?p ?o .
  ?p rdfs:domain ?class .
}
```
**Explanation**

Since the domain of _p_ is _class_, this implies that _resource_ is a _class_.

**Example**
```
sio:Role rdf:type owl:Class ;
    rdfs:label "role" ;
    rdfs:subClassOf sio:RealizableEntity ;
    dct:description "A role is a realizable entity that describes behaviours, rights and obligations of an entity in some particular circumstance." .

sio:isAttributeOf rdf:type owl:ObjectProperty ;
    rdfs:label "is attribute of" ;
    dct:description "is attribute of is a relation that associates an attribute with an entity where an attribute is an intrinsic characteristic such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier) either directly or indirectly through generalization of entities of the same type." ;
    rdfs:subPropertyOf sio:isRelatedTo .

sio:hasAttribute rdf:type owl:ObjectProperty ;
    rdfs:label "has attribute" ;
    dct:description "has attribute is a relation that associates a entity with an attribute where an attribute is an intrinsic characteristic such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier) either directly or indirectly through generalization of entities of the same type." ;
    rdfs:subPropertyOf sio:isRelatedTo .

sio:isPropertyOf rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "is property of" ;
    dct:description "is property of is a relation betweena  quality, capability or role and the entity that it and it alone bears." ;
    rdfs:subPropertyOf sio:isAttributeOf .

sio:hasProperty rdf:type owl:ObjectProperty ,
                                owl:InverseFunctionalProperty;
    rdfs:label "has property" ;
    owl:inverseOf sio:isPropertyOf ;
    dct:description "has property is a relation between an entity and the quality, capability or role that it and it alone bears." ;
    rdfs:subPropertyOf sio:hasAttribute .

sio:hasRealizableProperty rdf:type owl:ObjectProperty ,
                                owl:InverseFunctionalProperty;
    rdfs:label "has realizable property" ;
    rdfs:subPropertyOf sio:hasProperty .

sio:isRealizablePropertyOf rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "is realizable property of" ;
    rdfs:subPropertyOf sio:isPropertyOf ;
    owl:inverseOf sio:hasRealizableProperty .

sio:isRoleOf rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "is role of" ;
    rdfs:domain sio:Role ;
    rdfs:subPropertyOf sio:isRealizablePropertyOf ;
    dct:description "is role of is a relation between a role and the entity that it is a property of." ;
    owl:inverseOf sio:hasRole .

sio:hasRole rdf:type owl:ObjectProperty ,
                                owl:InverseFunctionalProperty;
    rdfs:label "has role" ;
    rdfs:subPropertyOf sio:hasRealizableProperty ;
    dct:description "has role is a relation between an entity and a role that it bears." .

sio:Human  rdf:type owl:Class ;
    rdfs:label "human" ;
    rdfs:subClassOf sio:MulticellularOrganism ;
    dct:description "A human is a primates of the family Hominidae and are characterized by having a large brain relative to body size, with a well developed neocortex, prefrontal cortex and temporal lobes, making them capable of abstract reasoning, language, introspection, problem solving and culture through social learning." .

sio:MulticellularOrganism  rdf:type owl:Class ;
    rdfs:label "multicellular organism" ;
    rdfs:subClassOf sio:CellularOrganism ;
    dct:description "A multi-cellular organism is an organism that consists of more than one cell." .

sio:CellularOrganism  rdf:type owl:Class ;
    rdfs:label "cellular organism" ;
    rdfs:subClassOf sio:Organism ;
    dct:description "A cellular organism is an organism that contains one or more cells." .

sio:Non-cellularOrganism  rdf:type owl:Class ;
    rdfs:label "non-cellular organism" ;
    rdfs:subClassOf sio:Organism ;
    dct:description "A non-cellular organism is an organism that does not contain a cell." .

sio:Organism rdf:type owl:Class ;
    owl:equivalentClass 
        [   rdf:type owl:Class ;
            owl:unionOf ( sio:CellularOrganism sio:Non-cellularOrganism ) ] ;
    rdfs:subClassOf sio:BiologicalEntity ;
    dct:description "A biological organisn is a biological entity that consists of one or more cells and is capable of genomic replication (independently or not)." ;
    rdfs:label "organism" .

sio:BiologicalEntity  rdf:type owl:Class ;
    rdfs:label "biological entity" ;
    rdfs:subClassOf sio:HeterogeneousSubstance ;
    dct:description "A biological entity is a heterogeneous substance that contains genomic material or is the product of a biological process." .

sio:HeterogeneousSubstance  rdf:type owl:Class ;
    rdfs:label "heterogeneous substance" ;
    rdfs:subClassOf sio:MaterialEntity ;
    rdfs:subClassOf sio:ChemicalEntity ;
    dct:description "A heterogeneous substance is a chemical substance that is composed of more than one different kind of component." .

sio:MaterialEntity  rdf:type owl:Class ;
    rdfs:label "material entity" ;
    rdfs:subClassOf sio:Object ;
    dct:description "A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass." .

sio:ChemicalEntity  rdf:type owl:Class ;
    rdfs:label "chemical entity" ;
    rdfs:subClassOf sio:MaterialEntity ;
    dct:description "A chemical entity is a material entity that pertains to chemistry." .

val-kb:Mother rdf:type owl:Individual ;
    rdfs:label "mother" ;
    sio:isRoleOf val-kb:Sarah ;
    sio:inRelationTo val-kb:Tim .

val-kb:Sarah rdf:type sio:Human ;
    rdfs:label "Sarah" .

val-kb:Tim rdf:type sio:Human ;
    rdfs:label "Tim" .
```
A reasoner should infer `val-kb:Mother rdf:type sio:Role .` and/or `val-kb:Sarah sio:hasRole val-kb:Mother .`
#### Property Range

**Axiom**
![formula](https://render.githubusercontent.com/render/math?math=\text{T}%20\sqsubseteq%20\forall%20R.C)
**Query**
```
CONSTRUCT {
  ?o rdf:type ?class .
}
WHERE {
  ?resource ?p ?o .
  ?p rdfs:range ?class .
}
```
**Explanation**

Since the range of _p_ is _class_, this implies that _o_ is a _class_.

**Example**
```
sio:UnitOfMeasurement rdf:type owl:Class ;
    rdfs:label "unit of measurement" ;
    rdfs:subClassOf sio:Quantity ;
    dct:description "A unit of measurement is a definite magnitude of a physical quantity, defined and adopted by convention and/or by law, that is used as a standard for measurement of the same physical quantity." .

sio:hasUnit rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has unit" ;
    owl:inverseOf sio:isUnitOf ;
    rdfs:range sio:UnitOfMeasurement ;
    rdfs:subPropertyOf sio:hasAttribute ;
    dct:description "has unit is a relation between a quantity and the unit it is a multiple of." .

sio:isUnitOf rdf:type owl:ObjectProperty ;
    rdfs:label "is unit of" ;
    rdfs:domain sio:UnitOfMeasurement ;
    rdfs:subPropertyOf sio:isAttributeOf ;
    dct:description "is unit of is a relation between a unit and a quantity that it is a multiple of." .

sio:Height rdf:type owl:Class ;
    rdfs:label "height" ;
    rdfs:subClassOf sio:1DExtentQuantity ;
    dct:description "Height is the one dimensional extent along the vertical projection of a 3D object from a base plane of reference." .

sio:1DExtentQuantity rdf:type owl:Class ;
    rdfs:label "1D extent quantity" ;
    rdfs:subClassOf sio:SpatialQuantity ;
    dct:description "A quantity that extends in single dimension." .

sio:SpatialQuantity rdf:type owl:Class ;
    rdfs:label "spatial quantity" ;
    rdfs:subClassOf sio:DimensionalQuantity ;
    dct:description "A spatial quantity is a quantity obtained from measuring the spatial extent of an entity." .

sio:DimensionalQuantity rdf:type owl:Class ;
    rdfs:label "dimensional quantity" ;
    rdfs:subClassOf sio:Quantity ,
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasUnit ;
            owl:someValuesFrom sio:UnitOfMeasurement ] ;
    dct:description "A dimensional quantity is a quantity that has an associated unit." .

val-kb:Tom rdf:type sio:Human ;
    rdfs:label "Tom" ;
    sio:hasAttribute val-kb:HeightOfTom .

val-kb:HeightOfTom rdf:type sio:Height ;
    sio:hasUnit val-kb:Meter .

val-kb:Meter rdf:type owl:Individual ;
    rdfs:label "meter" .
```
A reasoner should infer `val-kb:Meter rdf:type sio:UnitOfMeasurement .`
### Datatype
#### Datatype Restriction
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?dataProperty ?value .
  ?class rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Restriction ;
        owl:onProperty ?dataProperty ; 
        owl:someValuesFrom ?datatype ] .
  ?dataProperty rdf:type owl:DatatypeProperty .
  ?datatype rdf:type rdfs:Datatype ;
    owl:onDatatype ?restrictedDatatype ;
    owl:withRestrictions ?list .
  {
    ?list rdf:first ?min .
    ?list rdf:rest/rdf:first ?max .
    ?min xsd:minInclusive ?minValue .
    ?max xsd:maxInclusive ?maxValue .
  }
  UNION
  {
    ?list rdf:first ?max .
    ?list rdf:rest/rdf:first ?min .
    ?min xsd:minInclusive ?minValue .
    ?max xsd:maxInclusive ?maxValue .
  }
  FILTER(?value < ?minValue || ?value > ?maxValue)
}
```
**Explanation**

Since _class_ has a with restriction on datatype property _dataProperty_ to be within the range specified in _list_ with min value _minValue_ and max value _maxValue_, and _resource_ is of type _class_ and has a value _value_ for _dataProperty_ which is outside the specified range, an inconsistency occurs.

**Example**
```
sio:hasValue rdf:type owl:DatatypeProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has value" ;
    dct:description "A relation between a informational entity and its actual value (numeric, date, text, etc)." .

sio:ProbabilityMeasure rdf:type owl:Class ;
    rdfs:subClassOf sio:DimensionlessQuantity ;
    dct:description "A probability measure is quantity of how likely it is that some event will occur." ;
    rdfs:label "probability measure" .

sio:ProbabilityValue rdf:type owl:Class ;
    rdfs:subClassOf sio:ProbabilityMeasure ;
    rdfs:subClassOf
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasValue ;
            owl:someValuesFrom 
                [ rdf:type rdfs:Datatype ;
                    owl:onDatatype xsd:double ;
                    owl:withRestrictions ( [ xsd:minInclusive "0.0"^^xsd:double ] [ xsd:maxInclusive "1.0"^^xsd:double ] ) 
                ]
        ] ;
    dct:description "A p-value or probability value is the probability of obtaining a test statistic at least as extreme as the one that was actually observed, assuming that the null hypothesis is true" ;
    #<sio:hasSynonym xml:lang="en">p-value</sio:hasSynonym>
    rdfs:label "probability value" .

val-kb:EffortExerted rdf:type sio:ProbabilityValue ;
    rdfs:label "effort exerted" ;
    sio:hasValue "1.1"^^xsd:double .
```
A reasoner should infer `val-kb:EffortExerted rdf:type owl:Nothing .` or that an inconsistency occurs.
### Assertions
#### Same Individual
**Axiom**

**Query**
```
CONSTRUCT {
  ?individual ?p ?o .
}
WHERE {
  {
    ?resource owl:sameAs ?individual .
  }
  UNION
  {
    ?individual owl:sameAs ?resource .
  }
  ?resource ?p ?o .
}
```
**Explanation**

Since _resource_ is the same as _individual_, they share the same properties.

**Example**
```
val-kb:Peter rdf:type sio:Human ;
    rdfs:label "Peter" ;
    sio:isRelatedTo val-kb:Samantha .

val-kb:Samantha rdf:type sio:Human ;
    rdfs:label "Samantha" .

val-kb:Peter owl:sameAs val-kb:Pete .
```
A reasoner should infer `val-kb:Pete rdf:type sio:Human ; rdfs:label "Peter" ; sio:isRelatedTo val-kb:Samantha .`
#### Different Individuals
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  {
    ?resource owl:differentFrom ?individual .
  }
  UNION
  {
    ?individual owl:differentFrom ?resource .
  }
  ?resource owl:sameAs ?individual .
}
```
**Explanation**

Since _resource_ is asserted as being different from _individual_, the assertion that _resource_ is the same as _individual_ leads to an inconsistency.

**Example**
```
val-kb:Sam owl:differentFrom val-kb:Samantha .
val-kb:Sam owl:sameAs val-kb:Samantha .
```
A reasoner should infer `val-kb:Sam rdf:type owl:Nothing .` or that an inconsistency occurs.
#### All Different Individuals
**Axiom**

**Query**
```
CONSTRUCT {
  ?member owl:differentFrom ?item .
}
WHERE {
  ?restriction rdf:type owl:AllDifferent ;
    owl:distinctMembers ?list .
  ?list rdf:rest*/rdf:first ?member .
  {
    SELECT DISTINCT ?item ?restrict WHERE
    {
      ?restrict rdf:type owl:AllDifferent ;
        owl:distinctMembers ?list .
      ?list rdf:rest*/rdf:first ?item .
    }
  }
  BIND(?restriction AS ?restrict) 
  FILTER(?member != ?item)
}
```
**Explanation**

Since _restriction_ is an all different restriction with individuals listed in _list_, each member in _list_ is different from each other member in the list.

**Example**
```
val-kb:DistinctTypesRestriction rdf:type owl:AllDifferent ;
    owl:distinctMembers
        ( val-kb:Integer
        val-kb:String 
        val-kb:Boolean
        val-kb:Double 
        val-kb:Float 
        val-kb:Tuple 
        ) .
```
A reasoner should infer
```
val-kb:Integer owl:differentFrom 
    val-kb:String , val-kb:Boolean, val-kb:Double , val-kb:Float , val-kb:Tuple .
val-kb:String owl:differentFrom 
    val-kb:Integer , val-kb:Boolean, val-kb:Double, val-kb:Float , val-kb:Tuple .
val-kb:Boolean owl:differentFrom 
    val-kb:Integer , val-kb:String, val-kb:Double, val-kb:Float , val-kb:Tuple .
val-kb:Double owl:differentFrom 
    val-kb:Integer , val-kb:String , val-kb:Boolean, val-kb:Float , val-kb:Tuple .
val-kb:Float owl:differentFrom 
    val-kb:Integer , val-kb:String , val-kb:Boolean, val-kb:Double , val-kb:Tuple .
val-kb:Tuple owl:differentFrom 
    val-kb:Integer , val-kb:String , val-kb:Boolean, val-kb:Double, val-kb:Float .
```
#### Class Assertion
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type ?superClass .
}
WHERE {
  ?resource rdf:type ?class .
  ?class rdf:type owl:Class ;
    rdfs:subClassOf+ ?superClass .
}
```
**Explanation**

Since _class_ is a subclass of _superClass_, any individual that is an instance of _class_ is also an instance of _superClass_. Therefore, _resource_ is an instance of _superClass_.

**Example**
```
sio:Entity rdf:type owl:Class ;
    rdfs:label "entity" ;
    dct:description "Every thing is an entity." .

sio:Attribute rdf:type owl:Class ;
    rdfs:subClassOf sio:Entity ;
    rdfs:label "attribute" ;
    dct:description "An attribute is a characteristic of some entity." .

sio:RealizableEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Attribute ;
    dct:description "A realizable entity is an attribute that is exhibited under some condition and is realized in some process." ;
    rdfs:label "realizable entity" .

sio:Quality rdf:type owl:Class ;
    rdfs:subClassOf sio:Attribute ;
    owl:disjointWith sio:RealizableEntity ;
    dct:description "A quality is an attribute that is intrinsically associated with its bearer (or its parts), but whose presence/absence and observed/measured value may vary." ;
    rdfs:label "quality" .
    
val-kb:Reliable rdf:type sio:Quality ;
    rdfs:label "reliable" .
```
A reasoner should infer `val-kb:Reliable rdf:type sio:Attribute , sio:Entity .`

#### Property Assertion
**Axiom**

**Query**
```
CONSTRUCT {
}
WHERE {
}
```
**Explanation**


**Example**

```
```
A reasoner should infer ` `
##### Object Property Assertion
**Axiom**

**Query**
```
CONSTRUCT {
}
WHERE {
}
```
**Explanation**


**Example**

```
```
A reasoner should infer ` `
##### Data Property Assertion
**Axiom**


**Query**

```
CONSTRUCT {
}
WHERE {
}
```
**Explanation**


**Example**

```
```
A reasoner should infer ` `
##### Negative Object Property Assertion
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?p ?o.
  ?p rdf:type owl:ObjectProperty .
  ?x rdf:type owl:NegativePropertyAssertion ;
    owl:sourceIndividual ?resource ;
    owl:assertionProperty ?p ;
    owl:targetIndividual ?o .
}
```
**Explanation**

Since a negative object property assertion was made with source _resource_, object property _p_, and target individual _o_, the existence of _resource_ _p_ _o_ results in an inconsistency.

**Example**
```
sio:hasAttribute rdf:type owl:ObjectProperty ;
    rdfs:label "has attribute" ;
    dct:description "has attribute is a relation that associates a entity with an attribute where an attribute is an intrinsic characteristic such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier) either directly or indirectly through generalization of entities of the same type." ;
    rdfs:subPropertyOf sio:isRelatedTo .

sio:hasUnit rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has unit" ;
    owl:inverseOf sio:isUnitOf ;
    rdfs:range sio:UnitOfMeasurement ;
    rdfs:subPropertyOf sio:hasAttribute ;
    dct:description "has unit is a relation between a quantity and the unit it is a multiple of." .

ex-kb:AgeOfSamantha rdf:type sio:Age ;
    rdfs:label "Samantha's age" .

ex-kb:NOPA rdf:type owl:NegativePropertyAssertion ; 
    owl:sourceIndividual ex-kb:AgeOfSamantha ; 
    owl:assertionProperty sio:hasUnit ; 
    owl:targetIndividual ex-kb:Meter .

ex-kb:AgeOfSamantha sio:hasUnit ex-kb:Meter .
```
A reasoner should infer `ex-kb:AgeOfSamantha rdf:type owl:Nothing .` or that an inconsistency occurs.

##### Negative Data Property Assertion
**Axiom**

**Query**

```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?p ?o.
  ?p rdf:type owl:DatatypeProperty .
  ?x rdf:type owl:NegativePropertyAssertion ;
    owl:sourceIndividual ?resource ;
    owl:assertionProperty ?p ;
    owl:targetValue ?o .
}
```
**Explanation**

Since a negative datatype property assertion was made with source _resource_, datatype property _p_, and target value _o_, the existence of _resource_ _p_ _o_ results in an inconsistency.

**Example**
```
val-kb:NDPA rdf:type owl:NegativePropertyAssertion ; 
    owl:sourceIndividual val-kb:AgeOfPeter ; 
    owl:assertionProperty sio:hasValue ; 
    owl:targetValue "10" .

val-kb:AgeOfPeter rdf:type sio:Age;
    rdfs:label "Peter's age" ;
    sio:hasValue "10" .
```
A reasoner should infer `val-kb:AgeOfPeter rdf:type owl:Nothing .` or that an inconsistency occurs.
### Keys
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource owl:sameAs ?individual .
}
WHERE {
  ?resource rdf:type ?class ;
    ?keyProperty ?keyValue.
  ?class rdf:type owl:Class ;
    owl:hasKey ( ?keyProperty ) .
  ?individual rdf:type ?class ;
    ?keyProperty ?keyValue.
}
```
**Explanation**

Since _class_ has key _keyProperty_, _resource_ and _individual_ are both of type _class_, and _resource_ and _individual_ both _keyProperty_ _keyValue_, then _resource_ and _individual_ must be the same.

**Example**
```
valo:uniqueID rdf:type owl:DatatypeProperty ;
    rdfs:label "unique identifier" .

valo:Person rdf:type owl:Class ;
    rdfs:subClassOf sio:Human ;
    rdfs:label "person" ;
    owl:hasKey ( valo:uniqueID ) .

val-kb:John rdf:type valo:Person ;
    rdfs:label "John" ;
    valo:uniqueID "101D" .

val-kb:Jack rdf:type valo:Person ;
    rdfs:label "Jack" ;
    valo:uniqueID "101D" .
```
A reasoner should infer `val-kb:John owl:sameAs val-kb:Jack .`
### Existential Quantification
#### Object Some Values From
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=\exists%20P.C)

**Query**
```
CONSTRUCT {
  ?resource rdf:type ?class .
}
WHERE {
  ?resource ?objectProperty
    [ rdf:type ?valueclass ] .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction;
      owl:onProperty ?objectProperty;
      owl:someValuesFrom ?valueclass ] .
}
```
**Explanation**

Since _resource_ _objectProperty_ an instance of _valueclass_, and _class_ has a restriction on _objectProperty_ to have some values from _valueclass_, we can infer that _resource_ rdf:type _class_.

**Example**

```
sio:CollectionOf3dMolecularStructureModels rdf:type owl:Class ;
    rdfs:subClassOf sio:Collection ,
        [ rdf:type owl:Restriction ;
        owl:onProperty sio:hasMember ;
        owl:someValuesFrom sio:3dStructureModel ] ;
    rdfs:label "collection of 3d molecular structure models" ;
    dct:description "A collection of 3D molecular structure models is just that." .

sio:3dStructureModel rdf:type owl:Class ;
    rdfs:subClassOf sio:TertiaryStructureDescriptor ;
    rdfs:label "3d structure model" ;
    dct:description "A 3D structure model is a representation of the spatial arrangement of one or more chemical entities." .

sio:TertiaryStructureDescriptor rdf:type owl:Class ;
    rdfs:subClassOf sio:BiomolecularStructureDescriptor ;
    rdfs:label "tertiary structure descriptor" ;
    dct:description "A tertiary structure descriptor describes 3D topological patterns in a biopolymer." .

sio:BiomolecularStructureDescriptor rdf:type owl:Class ;
    rdfs:subClassOf sio:MolecularStructureDescriptor ;
    rdfs:label "biomolecular structure descriptor" ;
    dct:description "A biomolecular structure descriptor is structure description for organic compounds." .

sio:MolecularStructureDescriptor rdf:type owl:Class ;
    rdfs:subClassOf sio:ChemicalQuality ;
    rdfs:label "molecular structure descriptor" ;
    dct:description "A molecular structure descriptor is data that describes some aspect of the molecular structure (composition) and is about some chemical entity." .

sio:ChemicalQuality rdf:type owl:Class ;
    rdfs:subClassOf sio:ObjectQuality ;
    rdfs:label "chemical quality" ;
    dct:description "Chemical quality is the quality of a chemical entity." .

sio:ObjectQuality rdf:type owl:Class ;
    rdfs:subClassOf sio:Quality ;
    rdfs:label "object quality" ;
    dct:description "An object quality is quality of an object." .

val-kb:MolecularCollection rdf:type owl:Individual ;
    rdfs:label "molecular collection" ;
    sio:hasMember val-kb:WaterMolecule .

val-kb:WaterMolecule rdf:type sio:3dStructureModel  .
```
A reasoner should infer `val-kb:MolecularCollection rdf:type sio:CollectionOf3dMolecularStructureModels .`
#### Data Some Values From

**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?datatypeProperty ?val .
  ?datatypeProperty rdf:type owl:DatatypeProperty .
  ?class rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Restriction ;
        owl:onProperty ?datatypeProperty ;
        owl:someValuesFrom ?value ] .
  FILTER(DATATYPE(?val) != ?value)
}
```
**Explanation**

_resource_ _datatypeProperty_ _val_, but _val_ does not have the same datatype _value_ restricted for _datatypeProperty_ in _class_. Since _resource_ rdf:type _class_, an inconsistency occurs.

**Example**
```
valo:Text rdf:type owl:Class ;
    rdfs:subClassOf
        [ rdf:type owl:Restriction ;
        owl:onProperty sio:hasValue  ;
        owl:someValuesFrom xsd:string ] .

val-kb:Question rdf:type valo:Text ;
    sio:hasValue "4"^^xsd:integer .
```
A reasoner should infer `val-kb:Question rdf:type owl:Nothing .` or that an inconsistency occurs.
#### Object Has Value
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource ?objectProperty ?object .
}
WHERE {
  ?resource rdf:type ?class .
  ?objectProperty rdf:type owl:ObjectProperty.
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ;
      owl:hasValue ?object ] .
}
```
**Explanation**

Since _resource_ is of type _class_, which has a value restriction on _objectProperty_ to have _object_, we can infer that _resource_ _objectProperty_ _object_.

**Example**
```
sio:isRelatedTo rdf:type owl:ObjectProperty ,
                                owl:SymmetricProperty ;
    rdfs:label "is related to" ;
    dct:description "A is related to B iff there is some relation between A and B." .

sio:isSpatiotemporallyRelatedTo rdf:type owl:ObjectProperty ,
                                owl:SymmetricProperty ;
    rdfs:subPropertyOf sio:isRelatedTo ;
    rdfs:label "is spatiotemporally related to" ;
    dct:description "A is spatiotemporally related to B iff A is in the spatial or temporal vicinity of B" .

sio:isLocationOf rdf:type owl:ObjectProperty ,
                                owl:TransitiveProperty ;
    rdfs:subPropertyOf sio:isSpatiotemporallyRelatedTo ;
    rdfs:label "is location of" ;
    dct:description "A is location of B iff the spatial region occupied by A has the spatial region occupied by B as a part." .

sio:hasPart rdf:type owl:ObjectProperty ,
                                owl:TransitiveProperty ,
                                owl:ReflexiveProperty ;
    rdfs:subPropertyOf sio:isLocationOf ;
    owl:inverseOf sio:isPartOf ;
    rdfs:label "has part" ;
    dct:description "has part is a transitive, reflexive and antisymmetric relation between a whole and itself or a whole and its part" .

valo:Vehicle rdf:type owl:Class ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasPart ;
            owl:hasValue val-kb:Wheel ] .

val-kb:Car rdf:type ex:Vehicle ;
    sio:hasPart ex-kb:Mirror .

val-kb:Mirror owl:differentFrom ex-kb:Wheel .
```
A reasoner should infer `val-kb:Car sio:hasPart val-kb:Wheel .`
#### Data Has Value
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type ?class .
}
WHERE {
  ?resource ?datatypeProperty ?value.
  ?datatypeProperty rdf:type owl:DatatypeProperty .
  ?class owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?datatypeProperty ;
      owl:hasValue ?value ].
}
```
**Explanation**

Since _class_ is equivalent to the restriction on _datatypeProperty_ to have value _value_ and _resource_ _datatypeProperty_ _value_, we can infer that _resource_ _rdf:type_ _class_.

**Example**

```
sio:hasValue rdf:type owl:DatatypeProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has value" ;
    dct:description "A relation between a informational entity and its actual value (numeric, date, text, etc)." .
    
valo:hasAge rdf:type owl:DatatypeProperty ;
    rdfs:label "has age" ;
    rdfs:subPropertyOf sio:hasValue .
    
valo:Unliked rdf:type owl:Class ;
    owl:equivalentClass#rdfs:subClassOf
        [ rdf:type owl:Restriction ;
            owl:onProperty valo:hasAge ;
            owl:hasValue "23"^^xsd:integer ] .

val-kb:Tom valo:hasAge "23"^^xsd:integer .
```
A reasoner should infer `val-kb:Tom rdf:type ex:Unliked .`
### Universal Quantification
#### Object All Values From
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=\forall%20P.C)

**Query**
```
CONSTRUCT {
  ?resource rdf:type ?valueclass.
}
WHERE {
  ?individual rdf:type ?class ; 
    ?objectProperty ?resource .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction;
      owl:onProperty ?objectProperty;
      owl:allValuesFrom ?valueclass ] .
}
```
**Explanation**

Since _class_ has a restriction on _objectProperty_ to have all values from _valueclass_, _individual_ _rdf:type_ _class_, and _individual_ _objectProperty_ _resource_, we can infer that _resource_ _rdf:type_ _valueclass_.

**Example**
```
sio:Namespace rdf:type owl:Class ;
    rdfs:subClassOf sio:ComputationalEntity ,
        [ rdf:type owl:Restriction ;
        owl:onProperty sio:hasMember ;
        owl:allValuesFrom sio:Identifier ] ;
    rdfs:label "namespace" ;
    dct:description "A namespace is an informational entity that defines a logical container for a set of symbols or identifiers." .

sio:ComputationalEntity rdf:type owl:Class;
    rdfs:subClassOf sio:InformationContentEntity ;
    rdfs:label "computational entity" ;
    dct:description "A computational entity is an information content entity operated on using some computational system." .

val-kb:NamespaceInstance rdf:type sio:Namespace ;
    sio:hasMember val-kb:NamespaceID .
```
A reasoner should infer `val-kb:NamespaceID rdf:type sio:Identifier .`
#### Data All Values From
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?datatypeProperty ?val .
  ?datatypeProperty rdf:type owl:DatatypeProperty .
  ?class rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Restriction ;
        owl:onProperty ?datatypeProperty ;
        owl:allValuesFrom ?value ] .
  FILTER(DATATYPE(?val)!= ?value)
}
```
**Explanation**

_resource_ _datatypeProperty_ _val_, but _val_ does not have the same datatype _value_ restricted for _datatypeProperty_ in _class_. Since _resource_ _rdf:type_ _class_, an inconsistency occurs.

**Example**
```
valo:Integer rdf:type owl:Class ;
    rdfs:subClassOf sio:ComputationalEntity ,
        [ rdf:type owl:Restriction ;
        owl:onProperty sio:hasValue ;
        owl:allValuesFrom xsd:integer ] ;
    rdfs:label "integer" .

val-kb:Ten rdf:type valo:Integer ;
    sio:hasValue "10.1"^^xsd:float .
```
A reasoner should infer `val-kb:Ten rdf:type owl:Nothing .` or than an inconsistency occurs.
### Self Restriction
#### Object Has Self
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource ?objectProperty ?resource .
}
WHERE {
  ?resource rdf:type ?class .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ;
      owl:hasSelf \"true\"^^xsd:boolean ] .
}
```
**Explanation**

_resource_ is of type _class_, which has a self restriction on the property _objectProperty_, allowing us to infer _resource_ _objectProperty_ _resource_.

**Example**

```
valo:SelfAttributing rdf:type owl:Class ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasAttribute ;
            owl:hasSelf "true"^^xsd:boolean ] .

val-kb:Blue rdf:type valo:SelfAttributing .
```
A reasoner should infer `val-kb:Blue sio:hasAttribute val-kb:Blue .`
### Individual Enumeration
#### Object One Of
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=\{x_1\}\sqcup\dots\sqcup\{x_n\})

##### Object One Of Membership
**Query**
```
CONSTRUCT {
  ?member rdf:type ?resource .
}
WHERE {
  ?resource rdf:type owl:Class ;
    owl:oneOf ?list .
  ?list rdf:rest*/rdf:first ?member .
}
```
**Explanation**

Since _resource_ has a one of relationship with _list_, the member _member_ in _list_ is of type _resource_.

**Example**
```
valo:Type rdf:type owl:Class ;
    owl:oneOf (val-kb:Integer val-kb:String val-kb:Boolean val-kb:Double val-kb:Float) .

val-kb:DistinctTypesRestriction rdf:type owl:AllDifferent ;
    owl:distinctMembers
        ( val-kb:Integer
        val-kb:String 
        val-kb:Boolean
        val-kb:Double 
        val-kb:Float 
        val-kb:Tuple 
        ) .
```
A reasoner should infer `val-kb:Integer rdf:type valo:Type . val-kb:String rdf:type valo:Type . val-kb:Boolean rdf:type valo:Type . val-kb:Double rdf:type valo:Type . val-kb:Float rdf:type valo:Type .`
##### Object One Of Inconsistency
**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?class rdf:type owl:Class ;
    owl:oneOf ?list .
  ?list rdf:rest*/rdf:first ?member .
  ?resource rdf:type ?class .
  {
    SELECT DISTINCT (COUNT(DISTINCT ?concept) AS ?conceptCount)
    WHERE 
    {
      ?concept rdf:type owl:Class ;
        owl:oneOf ?list .
      ?individual rdf:type ?concept .
      ?list rdf:rest*/rdf:first ?member .
      FILTER(?individual = ?member)
    }
  }
  FILTER(?conceptCount=0)
}
```
**Explanation**

Since _class_ has a one of relationship with _list_, and _resource_ is not in _list_, the assertion _resource_ is a _class_ leads to an inconsistency.

**Example**
```
valo:Type rdf:type owl:Class ;
    owl:oneOf (val-kb:Integer val-kb:String val-kb:Boolean val-kb:Double val-kb:Float) .

val-kb:DistinctTypesRestriction rdf:type owl:AllDifferent ;
    owl:distinctMembers
        ( val-kb:Integer
        val-kb:String 
        val-kb:Boolean
        val-kb:Double 
        val-kb:Float 
        val-kb:Tuple 
        ) .

val-kb:Tuple rdf:type valo:Type .
```
A reasoner should infer `val-kb:Tuple rdf:type owl:Nothing .` or that an inconsistency occurs.
#### Data One Of
**Axiom**


**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?datatypeProperty rdf:type owl:DatatypeProperty ;
    rdfs:range [ rdf:type owl:DataRange ;
      owl:oneOf ?list ] .
  ?resource ?datatypeProperty ?value .
  ?list rdf:rest*/rdf:first ?member .
  {
    SELECT DISTINCT (COUNT( DISTINCT ?datatypeProperty) AS ?dataCount)
    WHERE 
    {
      ?datatypeProperty rdf:type owl:DatatypeProperty ;
      rdfs:range [ rdf:type owl:DataRange ;
        owl:oneOf ?list ] .
      ?individual ?datatypeProperty ?value .
      ?list rdf:rest*/rdf:first ?member .
      FILTER(?value=?member)
    }
  }
  FILTER(?dataCount=0)
}
```
**Explanation**

Since _datatypeProperty_ is restricted to have a value from _list_, and _resource_ _datatypeProperty_ _value_, but _value_ is not in _list_, an inconsistency occurs.

**Example**
```
valo:hasTeenAge rdf:type owl:DatatypeProperty ;
    rdfs:label "has age" ;
    rdfs:range [ rdf:type owl:DataRange ;
        owl:oneOf ("13"^^xsd:integer "14"^^xsd:integer "15"^^xsd:integer "16"^^xsd:integer "17"^^xsd:integer "18"^^xsd:integer "19"^^xsd:integer )].

val-kb:Sarah valo:hasTeenAge "12"^^xsd:integer .
```
A reasoner should infer `val-kb:Sarah rdf:type owl:Nothing .` or that an inconsistency occurs.
### Cardinality
#### Max Cardinality
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=\leq%20nP)

##### Object Max Cardinality

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?objectProperty ?object .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ;
      owl:maxCardinality ?cardinalityValue ].
  {
    SELECT DISTINCT (COUNT(DISTINCT ?object) AS ?objectCount) ?individual ?concept
    WHERE 
    {
      ?individual rdf:type ?concept ;
        ?objectProperty ?object .
      ?objectProperty rdf:type owl:ObjectProperty .
      ?concept rdfs:subClassOf|owl:equivalentClass
        [ rdf:type owl:Restriction ;
          owl:onProperty ?objectProperty ;
          owl:maxCardinality ?cardinalityValue ].
    } GROUP BY ?individual ?concept
  }
  BIND(?resource AS ?individual)
  BIND(?class AS ?concept)
  FILTER(?objectCount > ?cardinalityValue)
}
```
**Explanation**

Since _objectProperty_ is assigned a maximum cardinality of _cardinalityValue_ for class _class_, _resource_ _rdf:type_ _class_, and _resource_ has _objectCount_ distinct assignments of _objectProperty_ which is greater than _cardinalityValue_, we can conclude that there is an inconsistency associated with _resource_.

**Example**
```
valo:DeadlySins rdf:type owl:Class ;
    rdfs:subClassOf sio:Collection ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasMember ;
            owl:maxCardinality "7"^^xsd:integer ] ;
    rdfs:label "seven deadly sins" .

val-kb:SevenDeadlySins rdf:type valo:DeadlySins ;
    sio:hasMember 
        val-kb:Pride ,
        val-kb:Envy ,
        val-kb:Gluttony ,
        val-kb:Greed ,
        val-kb:Lust ,
        val-kb:Sloth ,
        val-kb:Wrath ,
        val-kb:Redundancy .

val-kb:DistinctSinsRestriction rdf:type owl:AllDifferent ;
    owl:distinctMembers
        (val-kb:Pride 
        val-kb:Envy 
        val-kb:Gluttony 
        val-kb:Greed 
        val-kb:Lust 
        val-kb:Sloth 
        val-kb:Wrath 
        val-kb:Redundancy ) .
```
##### Data Max Cardinality

**Query**

```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?dataProperty ?data .
  ?dataProperty rdf:type owl:DatatypeProperty .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?dataProperty ;
      owl:maxCardinality ?cardinalityValue ] .
  {
    SELECT DISTINCT (COUNT(DISTINCT ?data) AS ?dataCount)
    WHERE 
    {
      ?resource rdf:type ?class ;
        ?dataProperty ?data .
      ?dataProperty rdf:type owl:DatatypeProperty .
      ?class rdfs:subClassOf|owl:equivalentClass
        [ rdf:type owl:Restriction ;
          owl:onProperty ?dataProperty ;
          owl:maxCardinality ?cardinalityValue ].
    }
  }
  FILTER(?dataCount > ?cardinalityValue)
}
```
**Explanation**

Since _datatypeProperty_ is assigned a maximum cardinality of _cardinalityValue_ for class _class_, _resource_ _rdf:type_ _class_, and _resource_ has _dataCount_ distinct assignments of _datatypeProperty_ which is greater than _cardinalityValue_, we can conclude that there is an inconsistency associated with _resource_.

**Example**
```
valo:hasAge rdf:type owl:DatatypeProperty ;
    rdfs:label "has age" ;
    rdfs:subPropertyOf sio:hasValue .

valo:Person rdf:type owl:Class ;
    rdfs:label "person" ;
    rdfs:subClassOf
        [ rdf:type owl:Restriction ;
            owl:onProperty valo:hasAge ;
            owl:maxCardinality "1"^^xsd:integer ] . 

val-kb:Katie rdf:type valo:Person ;
    rdfs:label "Katie" ;
    valo:hasAge "31"^^xsd:integer , "34"^^xsd:integer .
```
##### Object Max Qualified Cardinality
**Axiom**


**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?objectProperty ?object .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?object rdf:type ?restrictedClass .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ;
      owl:onClass ?restrictedClass ;
      owl:maxQualifiedCardinality ?cardinalityValue ].
  {
    SELECT DISTINCT (COUNT(DISTINCT ?object) AS ?objectCount) ?individual ?concept
    WHERE 
    {
      ?individual rdf:type ?concept ;
        ?objectProperty ?object .
      ?object rdf:type ?restrictedClass .
      ?objectProperty rdf:type owl:ObjectProperty .
      ?concept rdfs:subClassOf|owl:equivalentClass
        [ rdf:type owl:Restriction ;
          owl:onProperty ?objectProperty ;
          owl:onClass ?restrictedClass ;
          owl:maxQualifiedCardinality ?cardinalityValue ].
    } GROUP BY ?individual ?concept
  }
  BIND(?resource AS ?individual)
  BIND(?class AS ?concept)
  FILTER(?objectCount > ?cardinalityValue)
}
```
**Explanation**
Since _class_ is constrained with a qualified max cardinality restriction on property \texttt{objectProperty} to have a max of _value_ objects of type class _restrictedClass_, and _resource_ is a _class_ but has _objectCount_ objects assigned to _objectProperty_ which is more than _value_, we can infer that an inconsistency occurs.

**Example**
```
sio:hasComponentPart rdf:type owl:ObjectProperty ;
    rdfs:label "has component part" .

sio:Triangle rdf:type owl:Class ;
    rdfs:subClassOf sio:Polygon ;
    dct:description "A triangle is a polygon composed of three points and three line segments, in which each point is fully connected to another point along through the line segment." ;
    rdfs:label "triangle" .

sio:LineSegment rdf:type owl:Class ;
    rdfs:subClassOf sio:Line ;
    dct:description "A line segment is a line and a part of a curve that is (inclusively) bounded by two terminal points." ;
    rdfs:label "line segment" .

sio:DirectedLineSegment rdf:type owl:Class ;
    rdfs:subClassOf sio:LineSegment ;
    dct:description "A directed line segment is a line segment that is contained by an ordered pair of endpoints (a start point and an endpoint)." ;
    rdfs:label "directed line segment" .

sio:ArrowedLineSegment rdf:type owl:Class ;
    rdfs:subClassOf sio:DirectedLineSegment ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasPart ;
            owl:someValuesFrom sio:Triangle ] ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasComponentPart ; 
            owl:maxQualifiedCardinality "2"^^xsd:nonNegativeInteger ;
            owl:onClass sio:Triangle ] ;
    dct:description "An arrowed line is a directed line segment in which one or both endpoints is tangentially part of a triangle that bisects the line." ;
    rdfs:label "arrowed line segment" .

val-kb:TripleArrowLineSegment rdf:type sio:ArrowedLineSegment ;
    rdfs:label "triple arrow line segment" ;
    sio:hasComponentPart
        val-kb:LineSegment ,
        val-kb:FirstArrow ,
        val-kb:SecondArrow ,
        val-kb:ThirdArrow .

val-kb:FirstArrow rdf:type sio:Triangle ;
    rdfs:label "first arrow" .

val-kb:SecondArrow rdf:type sio:Triangle ;
    rdfs:label "second arrow" .

val-kb:ThirdArrow rdf:type sio:Triangle ;
    rdfs:label "third arrow" .

val-kb:LineSegment rdf:type sio:LineSegment ;
    rdfs:label "line segment " .
    
val-kb:DistinctTrianglesRestriction rdf:type owl:AllDifferent ;
    owl:distinctMembers (ex-kb:FirstArrow ex-kb:SecondArrow ex-kb:ThirdArrow ) .
```
##### Data Max Qualified Cardinality
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?datatypeProperty ?value .
  ?datatypeProperty rdf:type owl:DatatypeProperty .
  ?restriction rdf:type owl:Restriction ;
    owl:onProperty ?datatypeProperty ;
    owl:maxQualifiedCardinality ?cardinalityValue ;
    owl:onDataRange ?datatype .
  {
    SELECT (COUNT(DISTINCT ?value) AS ?valueCount) ?individual WHERE
    {
      ?individual ?datatypeProperty ?value .
      ?datatypeProperty rdf:type owl:DatatypeProperty .
      ?restriction rdf:type owl:Restriction ;
        owl:onProperty ?datatypeProperty ;
        owl:maxQualifiedCardinality ?cardinalityValue ;
        owl:onDataRange ?datatype .
    } GROUP BY ?individual
  }
  BIND(?resource AS ?individual)
  FILTER(DATATYPE(?value) = ?datatype)
  FILTER(?valueCount > ?cardinalityValue)
}
```
**Explanation**
Since _datatypeProperty_ is constrained with a qualified max cardinality restriction on datatype _datatype_ to have a max of _cardinalityValue_ values, and _resource_ has _valueCount_ values of type _datatype_ for property _datatypeProperty_, an inconsistency occurs.

**Example**

```
sio:InformationContentEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Object ;
    rdfs:label "information content entity" ;
    dct:description "An information content entity is an object that requires some background knowledge or procedure to correctly interpret." .

sio:MathematicalEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:InformationContentEntity ;
    rdfs:label "mathematical entity" ;
    dct:description "A mathematical entity is an information content entity that are components of a mathematical system or can be defined in mathematical terms." .

valo:hasPolynomialRoot rdf:type owl:DatatypeProperty ;
    rdfs:subPropertyOf sio:hasValue ;
    rdfs:label "has polynomial root" .

val-kb:QuadraticPolynomialRootRestriction rdf:type owl:Restriction ;
    owl:onProperty valo:hasPolynomialRoot ;
    owl:maxQualifiedCardinality "2"^^xsd:integer ;
    owl:onDataRange xsd:decimal .

val-kb:QuadraticPolynomialInstance rdf:type sio:ConceptualEntity ;
    rdfs:label "quadratic polynomial instance" ;
    valo:hasPolynomialRoot "1.23"^^xsd:decimal , "3.45"^^xsd:decimal , "5.67"^^xsd:decimal .
```
#### Min Cardinality
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=\leq%20nP)

##### Object Min Cardinality

**Query**
```
CONSTRUCT {
  ?resource ?objectProperty 
    [ rdf:type owl:Individual ; 
      owl:differentFrom ?object ] .
}
WHERE {
  ?resource rdf:type ?class ;
    ?objectProperty ?object .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ;
      owl:minCardinality ?cardinalityValue ].
  {
    SELECT DISTINCT (COUNT(DISTINCT ?object) AS ?objectCount)
    WHERE 
    {
      ?resource rdf:type ?class ;
        ?objectProperty ?object .
      ?objectProperty rdf:type owl:ObjectProperty .
      ?class rdfs:subClassOf|owl:equivalentClass
        [ rdf:type owl:Restriction ;
          owl:onProperty ?objectProperty ;
          owl:minCardinality ?cardinalityValue ].
    }
  }
  FILTER(?objectCount < ?cardinalityValue)
}
```
**Explanation**

Since _objectProperty_ is assigned a minimum cardinality of _cardinalityValue_ for class _class_, _resource_ _rdf:type_ _class_, and _resource_ has _objectCount_ distinct assignments of _objectProperty_ which is less than _cardinalityValue_, we can conclude the existence of additional assignments of _objectProperty_ for _resource_.

**Example**
```
valo:StudyGroup rdf:type owl:Class ;
    rdfs:subClassOf sio:Collection ,
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasMember ;
            owl:minCardinality "3"^^xsd:integer ] ; 
    rdfs:label "study group" .

val-kb:StudyGroupInstance rdf:type valo:StudyGroup ;
    sio:hasMember 
        val-kb:Steve ,
        val-kb:Ali .

val-kb:Steve rdf:type sio:Human .
val-kb:Luis rdf:type sio:Human .
val-kb:Ali rdf:type sio:Human .

val-kb:DistinctStudentsRestriction rdf:type owl:AllDifferent ;
    owl:distinctMembers
        (val-kb:Steve 
        val-kb:Luis 
        val-kb:Ali ) .
```

##### Data Min Cardinality
**Axiom**


**Query**
```
CONSTRUCT {
  ?resource ?dataProperty [ rdf:type rdfs:Datatype ] .
}
WHERE {
  ?resource rdf:type ?class ;
    ?dataProperty ?data .
  ?dataProperty rdf:type owl:DatatypeProperty .
  ?class rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Restriction ;
        owl:onProperty ?dataProperty ;
        owl:minCardinality ?cardinalityValue ] .
  {
    SELECT DISTINCT (COUNT(DISTINCT ?data) AS ?dataCount)
    WHERE 
    {
      ?resource rdf:type ?class ;
        ?dataProperty ?data .
      ?dataProperty rdf:type owl:DatatypeProperty .
      ?class rdf:type owl:Class ;
        rdfs:subClassOf|owl:equivalentClass
          [ rdf:type owl:Restriction ;
            owl:onProperty ?dataProperty ;
            owl:minCardinality ?cardinalityValue ].
    }
  }
  FILTER(?dataCount < ?cardinalityValue)
}
```
**Explanation**

Since _dataProperty_ is assigned a minimum cardinality of _cardinalityValue_ for class _class_, _resource_ _rdf:type_ _class_, and _resource_ has _dataCount_ distinct assignments of _dataProperty_ which is less than _cardinalityValue_, we can conclude the existence of additional assignments of _dataProperty_ for _resource_.

**Example**
```
valo:hasBirthYear rdf:type owl:DatatypeProperty ;
    rdfs:subPropertyOf sio:hasValue ;
    rdfs:label "has birth year" .

valo:Person rdf:type owl:Class ;
    rdfs:label "person" ;
    rdfs:subClassOf sio:Human ;
    rdfs:subClassOf
        [ rdf:type owl:Restriction ;
            owl:onProperty valo:hasBirthYear ;
            owl:cardinality "1"^^xsd:integer ] . 

val-kb:Erik rdf:type valo:Person ;
    rdfs:label "Erik" ;
    valo:hasBirthYear "1988"^^xsd:integer , "1998"^^xsd:integer .
```

##### Object Min Qualified Cardinality
**Axiom**


**Query**

```
CONSTRUCT {
  ?resource ?objectProperty 
    [ rdf:type owl:Individual ; 
      owl:differentFrom ?object ] .
}
WHERE {
  ?resource rdf:type ?class ;
    ?objectProperty ?object .
  ?object rdf:type ?restrictedClass .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ; 
      owl:minQualifiedCardinality ?value ;
        owl:onClass ?restrictedClass ] .
  {
    SELECT (COUNT(DISTINCT ?object) AS ?objectCount) ?individual ?concept WHERE 
    {          
      ?individual rdf:type ?concept ;
        ?objectProperty ?object .
      ?object rdf:type ?restrictedClass .
      ?objectProperty rdf:type owl:ObjectProperty .
      ?concept rdfs:subClassOf|owl:equivalentClass
        [ rdf:type owl:Restriction ;
          owl:onProperty ?objectProperty ; 
          owl:minQualifiedCardinality ?value ;
          owl:onClass ?restrictedClass ] .
    } GROUP BY ?individual ?concept
  }
  BIND(?resource AS ?individual)
  BIND(?class AS ?concept)
  FILTER(?objectCount < ?value)
}
```
**Explanation**
Since _class_ is constrained with a qualified min cardinality restriction on property _objectProperty_ to have a min of _value_ objects of type class _restrictedClass_, and _resource_ is a _class_ but has _objectCount_ objects assigned to _objectProperty_ which is less than _value_, we can infer the existence of another object.

**Example**
```
sio:Polyline rdf:type owl:Class ;
    rdfs:subClassOf sio:GeometricEntity ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasComponentPart ; 
            owl:minQualifiedCardinality "2"^^xsd:nonNegativeInteger ;
            owl:onClass sio:LineSegment ] ;
    dct:description "A polyline is a connected sequence of line segments." ;
    rdfs:label "polyline" .

val-kb:PolylineSegment rdf:type sio:Polyline ;
    rdfs:label "polyline segment " ;
    sio:hasComponentPart val-kb:LineSegmentInstance .

val-kb:LineSegmentInstance rdf:type sio:LineSegment ;
    rdfs:label "line segment instance" .
```
##### Data Min Qualified Cardinality
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource ?datatypeProperty [ rdf:type rdfs:Datatype ] .
}
WHERE {
  ?resource ?datatypeProperty ?value .
  ?datatypeProperty rdf:type owl:DatatypeProperty .
  ?restriction rdf:type owl:Restriction ;
    owl:onProperty ?datatypeProperty ;
    owl:minQualifiedCardinality ?cardinalityValue ;
    owl:onDataRange ?datatype .
  {
    SELECT (COUNT(DISTINCT ?value) AS ?valueCount) ?individual WHERE
    {
      ?individual ?datatypeProperty ?value .
      ?datatypeProperty rdf:type owl:DatatypeProperty .
      ?restriction rdf:type owl:Restriction ;
        owl:onProperty ?datatypeProperty ;
        owl:minQualifiedCardinality ?cardinalityValue ;
        owl:onDataRange ?datatype .
    } GROUP BY ?individual
  }
  BIND(?resource AS ?individual)
  FILTER(DATATYPE(?value) = ?datatype)
  FILTER(?valueCount < ?cardinalityValue)
}
```
**Explanation**
Since _datatypeProperty_ is constrained with a qualified min cardinality restriction on datatype _datatype_ to have a min of _cardinalityValue_ values, and _resource_ has _valueCount_ values of type _datatype_ for property _datatypeProperty_, we can infer the existence of at least one more additional value.

**Example**
```
valo:hasName rdf:type owl:DatatypeProperty ;
    rdfs:subPropertyOf sio:hasName ;
    rdfs:label "has name" .

val-kb:NameRestriction rdf:type owl:Restriction ;
    owl:onProperty valo:hasName ;
    owl:minQualifiedCardinality "2"^^xsd:integer ;
    owl:onDataRange xsd:string .

val-kb:Jackson rdf:type sio:Human ;
    rdfs:label "Jackson" ;
    valo:hasName "Jackson"^^xsd:string .
```

#### Exact Cardinality
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math==nP)

##### Object Exact Cardinality

**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?objectProperty ?object .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ;
      owl:cardinality ?cardinalityValue ].
  {
    SELECT DISTINCT (COUNT(DISTINCT ?object) AS ?objectCount)
    WHERE 
    {
      ?individual rdf:type ?class ;
        ?objectProperty ?object .
      ?objectProperty rdf:type owl:ObjectProperty .
      ?class rdfs:subClassOf|owl:equivalentClass
        [ rdf:type owl:Restriction ;
          owl:onProperty ?objectProperty ;
          owl:cardinality ?cardinalityValue ].
    } GROUP BY ?individual
  }
  FILTER(?objectCount > ?cardinalityValue)
  BIND(?resource AS ?individual)
}
```
**Explanation**
Since _objectProperty_ is assigned an exact cardinality of _cardinalityValue_ for class _class_, _resource_ _rdf:type_ _class_, and _resource_ has _objectCount_ distinct assignments of _objectProperty_ which is greater than _cardinalityValue_, we can conclude that there is an inconsistency associated with _resource_.

**Example**
```
valo:Trio rdf:type owl:Class ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasMember ;
            owl:cardinality "2"^^xsd:integer
        ] .

val-kb:Stooges rdf:type valo:Trio ;
    sio:hasMember 
        val-kb:Larry ,
        val-kb:Moe ,
        val-kb:Curly .

val-kb:DistinctStoogesRestriction rdf:type owl:AllDifferent ;
    owl:distinctMembers
        ( val-kb:Larry 
        val-kb:Moe 
        val-kb:Curly ) .
```
##### Data Exact Cardinality
**Axiom**


**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?dataProperty ?data .
  ?dataProperty rdf:type owl:DatatypeProperty .
  ?class rdf:type owl:Class ; 
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Restriction ;
        owl:onProperty ?dataProperty ;
        owl:cardinality ?cardinalityValue ] .
  {
    SELECT DISTINCT (COUNT(DISTINCT ?data) AS ?dataCount)
    WHERE 
    {
      ?resource rdf:type ?class ;
        ?dataProperty ?data .
      ?dataProperty rdf:type owl:DatatypeProperty .
      ?class rdf:type owl:Class ;
        rdfs:subClassOf|owl:equivalentClass
          [ rdf:type owl:Restriction ;
            owl:onProperty ?dataProperty ;
            owl:cardinality ?cardinalityValue ].
    }
  }
  FILTER(?dataCount > ?cardinalityValue)
}
```
**Explanation**
Since _dataProperty_ is assigned an exact cardinality of _cardinalityValue_ for class _class_, _resource_ _rdf:type_ _class_, and _resource_ has _dataCount_ distinct assignments of _dataProperty_ which is greater than _cardinalityValue_, we can conclude that there is an inconsistency associated with _resource_.

**Example**
```
valo:hasBirthYear rdf:type owl:DatatypeProperty ;
    rdfs:subPropertyOf sio:hasValue ;
    rdfs:label "has birth year" .

valo:Person rdf:type owl:Class ;
    rdfs:label "person" ;
    rdfs:subClassOf sio:Human ;
    rdfs:subClassOf
        [ rdf:type owl:Restriction ;
            owl:onProperty ex:hasBirthYear ;
            owl:cardinality "1"^^xsd:integer ] . 

val-kb:Erik rdf:type valo:Person ;
    rdfs:label "Erik" ;
    valo:hasBirthYear "1988"^^xsd:integer , "1998"^^xsd:integer .
```
A reasoner should infer `val-kb:Erik rdf:type owl:Nothing .` or that an inconsistency occurs.
##### Object Exact Qualified Cardinality
**Axiom**


**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ;
    ?objectProperty ?object .
  ?objectProperty rdf:type owl:ObjectProperty .
  ?object rdf:type ?restrictedClass .
  ?class rdfs:subClassOf|owl:equivalentClass
    [ rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ;
      owl:onClass ?restrictedClass ;
      owl:qualifiedCardinality ?cardinalityValue ].
  {
    SELECT DISTINCT (COUNT(DISTINCT ?object) AS ?objectCount) ?individual ?concept
    WHERE 
    {
      ?individual rdf:type ?concept ;
        ?objectProperty ?object .
      ?object rdf:type ?restrictedClass .
      ?objectProperty rdf:type owl:ObjectProperty .
      ?concept rdfs:subClassOf|owl:equivalentClass
        [ rdf:type owl:Restriction ;
          owl:onProperty ?objectProperty ;
          owl:onClass ?restrictedClass ;
          owl:qualifiedCardinality ?cardinalityValue ].
    } GROUP BY ?individual ?concept
  }
  BIND(?resource AS ?individual)
  BIND(?class AS ?concept)
  FILTER(?objectCount > ?cardinalityValue)
}
```
**Explanation**
Since _class_ is constrained with a qualified cardinality restriction on property _objectProperty_ to have _value_ objects of type class _restrictedClass_, and _resource_ is a _class_ but has _objectCount_ objects assigned to _objectProperty_, an inconsistency occurs.

**Example**
```
sio:hasComponentPart rdf:type owl:ObjectProperty ;
    rdfs:label "has component part" .

sio:PolygonEdge rdf:type owl:Class ;
    rdfs:subClassOf sio:LineSegment ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:isPartOf ;
            owl:someValuesFrom sio:Polygon ] ;
    rdfs:subClassOf 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:hasComponentPart ; 
            owl:qualifiedCardinality "2"^^xsd:nonNegativeInteger ;
            owl:onClass sio:PolygonVertex ] ;
    dct:description "A polygon edge is a line segment joining two polygon vertices." ;
    rdfs:label "polygon edge" .

val-kb:TripleVertexedPolyEdge rdf:type sio:PolygonEdge ;
    rdfs:label "triple vertexed polygon edge" ;
    sio:hasComponentPart val-kb:VertexOne , val-kb:VertexTwo , val-kb:VertexThree .

val-kb:VertexOne rdf:type sio:PolygonVertex ;
    rdfs:label "vertex one" .

val-kb:VertexTwo rdf:type sio:PolygonVertex ;
    rdfs:label "vertex two" .

val-kb:VertexThree rdf:type sio:PolygonVertex ;
    rdfs:label "vertex three" .
```
##### Data Exact Qualified Cardinality
**Axiom**


**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource ?datatypeProperty ?value .
  ?datatypeProperty rdf:type owl:DatatypeProperty .
  ?restriction rdf:type owl:Restriction ;
    owl:onProperty ?datatypeProperty ;
    owl:onDataRange ?datatype ;
    owl:qualifiedCardinality ?cardinalityValue .
  {
    SELECT DISTINCT (COUNT(DISTINCT ?value) AS ?valueCount) ?individual WHERE
    {
      ?individual ?datatypeProperty ?value .
      ?datatypeProperty rdf:type owl:DatatypeProperty .
      ?restriction rdf:type owl:Restriction ;
        owl:onProperty ?datatypeProperty ;
        owl:onDataRange ?datatype ;
        owl:qualifiedCardinality ?cardinalityValue .
    } GROUP BY ?individual
  }
  BIND(?resource AS ?individual)
  FILTER(DATATYPE(?value) = ?datatype)
  FILTER(?valueCount > ?cardinalityValue)
}
```
**Explanation**
Since _datatypeProperty_ is constrained with a qualified cardinality restriction on datatype _datatype_ to have _cardinalityValue_ values, and _resource_ has _valueCount_ values of type _datatype_ for property _datatypeProperty_, an inconsistency occurs.

**Example**
```
sio:hasValue rdf:type owl:DatatypeProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has value" ;
    dct:description "A relation between a informational entity and its actual value (numeric, date, text, etc)." .

valo:uniqueUsername rdf:type owl:DatatypeProperty ;
    rdfs:subPropertyOf sio:hasValue ;
    rdfs:label "unique username" .

val-kb:UsernameRestriction rdf:type owl:Restriction ;
    owl:onProperty valo:uniqueUsername ;
    owl:qualifiedCardinality "1"^^xsd:integer ;
    owl:onDataRange xsd:string .

val-kb:Steve rdf:type sio:Human ;
    rdfs:label "Steve" ;
    valo:uniqueUsername "SteveTheGamer"^^xsd:string , "ScubaSteve508"^^xsd:string .
```

### Disjunction
#### Object Union Of
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=C_1%20\sqcup%20\dots%20\sqcup%20C_n)

**Query**
```
CONSTRUCT {
  ?member rdfs:subClassOf ?resource .
}
WHERE {
  ?resource rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Class ;
        owl:unionOf ?list ] .
  ?list rdf:rest*/rdf:first ?member .
}
```
**Explanation**

Since the class _resource_ has a subclass or equivalent class relation with a class that comprises the union of _list_, which contains member _member_, we can infer that _member_ is a subclass of _resource_.

**Example**
```
sio:InformationContentEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Object ;
#    rdfs:subClassOf rdf:nodeID="arc0158b21" ;
    rdfs:label "information content entity" ;
    dct:description "An information content entity is an object that requires some background knowledge or procedure to correctly interpret." .

sio:GeometricEntity rdf:type owl:Class ;
    rdfs:label "geometric entity" ;
    rdfs:subClassOf sio:InformationContentEntity ;
    dct:description "A geometric entity is an information content entity that pertains to the structure and topology of a space." .

sio:Curve rdf:type owl:Class ;
    rdfs:label "curve" ;
    rdfs:subClassOf sio:GeometricEntity ;
    dct:description "A curve is a geometric entity that may be located in n-dimensional spatial region whose extension may be n-dimensional,  is composed of at least two fully connected points and does not intersect itself." .

sio:Line rdf:type owl:Class ;
    rdfs:subClassOf sio:Curve ;
    rdfs:label "line" ;
    owl:equivalentClass 
        [   rdf:type owl:Class ;
            owl:unionOf ( sio:LineSegment sio:Ray sio:InfiniteLine ) ] ;
    dct:description "A line is curve that extends in a single dimension (e.g. straight line; exhibits no curvature), and is composed of at least two fully connected points." .
```
A reasoner should infer `sio:LineSegment rdfs:subClassOf sio:Line . sio:Ray rdfs:subClassOf sio:Line . sio:InfiniteLine rdfs:subClassOf sio:Line .`
#### Data Union Of
**Axiom**

**Query**
```
CONSTRUCT {
  ?resource rdf:type ?class .
}
WHERE {
  ?class rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Class ;
        owl:unionOf ?list ] .
  ?list rdf:rest*/rdf:first ?member .
  ?member rdf:type owl:Restriction ;
    owl:onProperty ?dataProperty ;
    owl:someValuesFrom ?datatype . 
  ?dataProperty rdf:type owl:DatatypeProperty .
  ?resource ?dataProperty ?data .
  FILTER(DATATYPE(?data)=?datatype)
}
```
**Explanation**

Since _class_ has a subclass or equivalent class relationship to the union of _list_ which has members _member_, and _member_ is a restriction on _dataProperty_ to have some values from _datatype_, we can infer _resource_ _rdf:type_ _class_, since _resource_ _dataProperty_ _data_ and the datatype of _data_ is _datatype_.

**Example**
```
sio:hasValue rdf:type owl:DatatypeProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has value" ;
    dct:description "A relation between a informational entity and its actual value (numeric, date, text, etc)." .

sio:InformationContentEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Object ;
    rdfs:label "information content entity" ;
    dct:description "An information content entity is an object that requires some background knowledge or procedure to correctly interpret." .

sio:MathematicalEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:InformationContentEntity ;
    rdfs:label "mathematical entity" ;
    dct:description "A mathematical entity is an information content entity that are components of a mathematical system or can be defined in mathematical terms." .

sio:Number rdf:type owl:Class ;
    rdfs:label "number" ;
    rdfs:subClassOf sio:MathematicalEntity ;
    dct:description "A number is a mathematical object used to count, label, and measure." .

sio:MeasurementValue rdf:type owl:Class ;
    rdfs:label "measurement value" ;
    rdfs:subClassOf sio:Number ;
    rdfs:subClassOf 
        [ rdf:type owl:Class ;
            owl:unionOf ( 
                [ rdf:type owl:Restriction ; 
                    owl:onProperty sio:hasValue ;
                    owl:someValuesFrom xsd:dateTime ] 
                [ rdf:type owl:Restriction ; 
                    owl:onProperty sio:hasValue ;
                    owl:someValuesFrom xsd:double ]
                [ rdf:type owl:Restriction ; 
                    owl:onProperty sio:hasValue ;
                    owl:someValuesFrom xsd:float ]
                [ rdf:type owl:Restriction ; 
                    owl:onProperty sio:hasValue ;
                    owl:someValuesFrom xsd:integer ]
            ) ] ;
    dct:description "A measurement value is a quantitative description that reflects the magnitude of some attribute." .

val-kb:DateTimeMeasurement rdf:type owl:Individual ;
    rdfs:label "date time measurement" ;
    sio:hasValue "1990-10-14T21:32:52"^^xsd:dateTime .

val-kb:IntegerMeasurement rdf:type owl:Individual ;
    rdfs:label "integer measurement" ;
    sio:hasValue "12"^^xsd:integer .

val-kb:DoubleMeasurement rdf:type owl:Individual ;
    rdfs:label "double measurement" ;
    sio:hasValue "6.34"^^xsd:double .

val-kb:FloatMeasurement rdf:type owl:Individual ;
    rdfs:label "float measurement" ;
    sio:hasValue "3.14"^^xsd:float .
```
A reasoner should infer `val-kb:DateTimeMeasurement rdf:type sio:MeasurementValue . val-kb:IntegerMeasurement rdf:type sio:MeasurementValue . val-kb:DoubleMeasurement rdf:type sio:MeasurementValue . val-kb:FloatMeasurement rdf:type sio:MeasurementValue .`
#### Disjoint Union
**Axiom**

**Query**
```
CONSTRUCT {
  ?member rdfs:subClassOf ?resource ;
    owl:disjointWith ?item .
}
WHERE {
  ?resource rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Class ;
        owl:disjointUnionOf ?list ] .
  ?list rdf:rest*/rdf:first ?member .
  {
    SELECT DISTINCT ?item ?class WHERE 
    {
      ?class rdf:type owl:Class ;
        rdfs:subClassOf|owl:equivalentClass
          [ rdf:type owl:Class ;
            owl:disjointUnionOf ?list ] .
      ?list rdf:rest*/rdf:first ?item .
    }
  }
  FILTER(?resource = ?class)
  FILTER(?member != ?item)
}
```
**Explanation**

Since the class _resource_ has a subclass or equivalent class relation with a class that comprises the disjoint union of _list_, which contains member _member_, we can infer that _member_ is a subclass of _resource_ and disjoint with the other members of the list.

**Example**
```
sio:BiologicalEntity  rdf:type owl:Class ;
    rdfs:label "biological entity" ;
    rdfs:subClassOf sio:HeterogeneousSubstance ;
    dct:description "A biological entity is a heterogeneous substance that contains genomic material or is the product of a biological process." .

sio:HeterogeneousSubstance  rdf:type owl:Class ;
    rdfs:label "heterogeneous substance" ;
    rdfs:subClassOf sio:MaterialEntity ;
    rdfs:subClassOf sio:ChemicalEntity ;
    dct:description "A heterogeneous substance is a chemical substance that is composed of more than one different kind of component." .

sio:MaterialEntity  rdf:type owl:Class ;
    rdfs:label "material entity" ;
    rdfs:subClassOf sio:Object ;
    dct:description "A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass." .

sio:ChemicalEntity  rdf:type owl:Class ;
    rdfs:label "chemical entity" ;
    rdfs:subClassOf sio:MaterialEntity ;
    dct:description "A chemical entity is a material entity that pertains to chemistry." .

valo:Lobe rdf:type owl:Class ;
    rdfs:subClassOf sio:BiologicalEntity ;
    rdfs:label "lobe" ;
    dct:description "A lobe that is part the brain." ;
    owl:equivalentClass valo:LobeDisjointUnionClass .

valo:LobeDisjointUnionClass rdf:type owl:Class ;
    owl:disjointUnionOf ( ex:FrontalLobe ex:ParietalLobe ex:TemporalLobe ex:OccipitalLobe ex:LimbicLobe ) .
```
A reasoner should infer
```
valo:FrontalLobe rdfs:subClassOf valo:LobeDisjointUnionClass , valo:Lobe ;
    owl:disjointWith ex:ParietalLobe , valo:TemporalLobe , valo:OccipitalLobe , valo:LimbicLobe .

valo:ParietalLobe rdfs:subClassOf valo:LobeDisjointUnionClass , valo:Lobe ;
    owl:disjointWith valo:FrontalLobe , valo:TemporalLobe , valo:OccipitalLobe , valo:LimbicLobe .

valo:TemporalLobe rdfs:subClassOf valo:LobeDisjointUnionClass , valo:Lobe ;
    owl:disjointWith valo:FrontalLobe , valo:ParietalLobe , valo:OccipitalLobe , valo:LimbicLobe .

valo:OccipitalLobe rdfs:subClassOf valo:LobeDisjointUnionClass , valo:Lobe ;
    owl:disjointWith valo:FrontalLobe , valo:ParietalLobe , valo:TemporalLobe , valo:LimbicLobe .

valo:LimbicLobe rdfs:subClassOf valo:LobeDisjointUnionClass , valo:Lobe ;
    owl:disjointWith valo:FrontalLobe , valo:ParietalLobe , valo:TemporalLobe , valo:OccipitalLobe .
```
### Intersection
#### Object Intersection Of
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=C_1%20\sqcap%20\dots%20\sqcap%20C_n)
**Query**
```
CONSTRUCT {
  ?resource rdf:type ?class.
}
WHERE {
  ?class rdf:type owl:Class ;
    owl:intersectionOf ?list .
  ?list rdf:rest*/rdf:first ?member .
  {
    ?member rdf:type owl:Class .
    ?resource rdf:type ?member .
  }
  UNION 
  {
    ?member rdf:type owl:Restriction ;
      owl:onProperty ?objectProperty ;
      owl:someValuesFrom ?restrictedClass .
    ?objectProperty rdf:type owl:ObjectProperty .
    ?resource ?objectProperty [rdf:type  ?restrictedClass ] .
  }
  {
    SELECT DISTINCT * WHERE
    {
      ?concept rdf:type owl:Class ;
        owl:intersectionOf ?list .
      ?list rdf:rest*/rdf:first ?item .
      {
        ?item rdf:type owl:Class .
        ?individual rdf:type ?item .
      }
      UNION
      {
        ?item rdf:type owl:Restriction ;
          owl:onProperty ?objectProperty ;
          owl:someValuesFrom ?restrictedClass .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?individual ?objectProperty [rdf:type  ?restrictedClass ] .
      }
    }
  }
  BIND(?class AS ?concept) 
  BIND(?resource AS ?individual) 
  FILTER(?member != ?item)
}
```
**Explanation**

Since _class_ is the intersection of the the members in _list_, and _resource_ is of type each of the members in the list, then we can infer _resource_ is a _class_.

**Example**
```
sio:Molecule rdf:type owl:Class ;
    rdfs:label "molecule" .

sio:isTargetIn rdf:type owl:ObjectProperty ;
    rdfs:label "is target in" .

sio:Target rdf:type owl:Class  ;
    owl:intersectionOf ( 
        sio:Molecule 
        [ rdf:type owl:Restriction ;
            owl:onProperty sio:isTargetIn ;
            owl:someValuesFrom sio:Process ] ) ;
    rdfs:label "target" .

val-kb:ProteinReceptor rdf:type sio:Molecule ;
    rdfs:label "protein receptor" ;
    sio:isTargetIn val-kb:Therapy .

val-kb:Therapy rdf:type sio:Process ;
    rdfs:label "therapy" .
```
A reasoner should infer `val-kb:ProteinReceptor rdf:type sio:Target .`
```
val-kb:Brian rdf:type valo:CanTalk , valo:Dog , valo:Friendly .

valo:CanTalk rdf:type owl:Class .
valo:Dog rdf:type owl:Class .
valo:Friendly rdf:type owl:Class .

valo:FriendlyTalkingDog rdf:type owl:Class ;
    owl:intersectionOf (valo:CanTalk valo:Dog valo:Friendly) .
```
A reasoner should infer `val-kb:Brian rdf:type valo:FriendlyTalkingDog .`
#### Data Intersection Of
**Axiom**

**Query**
```
CONSTRUCT {
  
}
WHERE {
  
}
```
**Explanation**


**Example**

```
```

### Negation
#### Complement Of
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=\neg%20C)

##### Object Complement Of
**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?resource rdf:type ?class ,
      ?complementClass .
  ?class rdf:type owl:Class .
  ?complementClass rdf:type owl:Class .
  {?class owl:complementOf ?complementClass .} 
    UNION 
  {?complementClass owl:complementOf ?class .}
}
```
**Explanation**

Since _class_ and _complementClass_ are complementary, _resource_ being of type both _class_ and _complementClass_ leads to an inconsistency.

**Example**

```
valo:VitalStatus rdfs:subClassOf sio:Attribute ;
    rdfs:label "vital status" .

valo:Dead rdf:type owl:Class ;
    rdfs:subClassOf valo:VitalStatus ;
    rdfs:label "dead" .

valo:Alive rdf:type owl:Class ;
    rdfs:subClassOf valo:VitalStatus ;
    rdfs:label "alive" ;
    owl:complementOf valo:Dead .

val-kb:VitalStatusOfPat rdf:type valo:Alive , valo:Dead ;
    rdfs:label "Pat's Vital Status" ;
    sio:isAttributeOf val-kb:Pat .

val-kb:Pat rdf:type sio:Human ;
    rdfs:label "Pat" .
```
A reasoner should infer `val-kb:VitalStatusOfPat rdf:type owl:Nothing` or that an inconsistency occurs.
##### Data Complement Of
**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?datatype rdf:type rdfs:Datatype ;
    owl:datatypeComplementOf ?complement .
  ?resource ?dataProperty ?value .
  ?dataProperty rdf:type owl:DatatypeProperty ;
    rdfs:range ?datatype .
  FILTER(DATATYPE(?value) = ?complement)
}
```
**Explanation**

Since _datatype_ is the complement of _complement_, _dataProperty_ has range _datatype_, and _resource_ _dataProperty_ _value_, but _value_ is of type _complement_, an inconsistency occurs.

**Example**

```
```

##### Object Property Complement Of
**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?class rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Class ;
        owl:complementOf 
          [ rdf:type owl:Restriction ;
            owl:onProperty ?objectProperty ;
            owl:someValuesFrom ?restrictedClass ] 
      ] .
  ?resource rdf:type ?class ;
    ?objectProperty [ rdf:type ?objectClass ] .
  ?objectProperty rdf:type owl:ObjectProperty .
  {
    FILTER(?objectClass = ?restrictedClass)
  }
  UNION
  {
    ?objectClass rdfs:subClassOf*|owl:equivalentClass ?restrictedClass . 
  }
}
```
**Explanation**

Since _class_ is a subclass of or is equivalent to a class with a complement restriction on the use of _objectProperty_ to have values from _restrictedClass_, and _resource_ is of type _class_, but has the link _objectProperty_ to have values from an instance of _restrictedClass_, an inconsistency occurs.

**Example**
```
sio:hasUnit rdf:type owl:ObjectProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has unit" ;
    owl:inverseOf sio:isUnitOf ;
    rdfs:range sio:UnitOfMeasurement ;
    rdfs:subPropertyOf sio:hasAttribute ;
    dct:description "has unit is a relation between a quantity and the unit it is a multiple of." .

sio:DimensionlessQuantity rdf:type owl:Class ;
    rdfs:label "dimensionless quantity" ;
    rdfs:subClassOf sio:Quantity ,
        [ rdf:type owl:Class ;
            owl:complementOf [ rdf:type owl:Restriction ;
                owl:onProperty sio:hasUnit ;
                owl:someValuesFrom sio:UnitOfMeasurement ] ];
    owl:disjointWith sio:DimensionalQuantity ;
    dct:description "A dimensionless quantity is a quantity that has no associated unit." .

sio:Quantity rdf:type owl:Class ;
    rdfs:label "quantity" ;
    owl:equivalentClass 
        [ rdf:type owl:Class ; 
            owl:unionOf (sio:DimensionlessQuantity sio:DimensionalQuantity) ] ;
    rdfs:subClassOf sio:MeasurementValue ;
    dct:description "A quantity is an informational entity that gives the magnitude of a property." .

sio:MeasurementValue rdf:type owl:Class ;
    rdfs:label "measurement value" ;
    rdfs:subClassOf sio:Number ;
    dct:description "A measurement value is a quantitative description that reflects the magnitude of some attribute." .

sio:Number rdf:type owl:Class ;
    rdfs:label "number" ;
    rdfs:subClassOf sio:MathematicalEntity ;
    dct:description "A number is a mathematical object used to count, label, and measure." .

sio:MathematicalEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:InformationContentEntity ;
    rdfs:label "mathematical entity" ;
    dct:description "A mathematical entity is an information content entity that are components of a mathematical system or can be defined in mathematical terms." .

sio:InformationContentEntity rdf:type owl:Class ;
    rdfs:subClassOf sio:Object ;
    rdfs:label "information content entity" ;
    dct:description "An information content entity is an object that requires some background knowledge or procedure to correctly interpret." .

val-kb:Efficiency rdf:type sio:DimensionlessQuantity  ;
    sio:hasUnit [ rdf:type valo:Percentage ] ;
    rdfs:label "efficiency" .

valo:Percentage rdfs:subClassOf sio:UnitOfMeasurement ;
    rdfs:label "percentage" .
```
A reasoner should infer `val-kb:Efficiency rdf:type owl:Nothing .`
##### Data Property Complement Of
**Query**
```
CONSTRUCT {
  ?resource rdf:type owl:Nothing .
}
WHERE {
  ?class rdf:type owl:Class ;
    rdfs:subClassOf|owl:equivalentClass
      [ rdf:type owl:Class ;
        owl:complementOf 
          [ rdf:type owl:Restriction ;
            owl:onProperty ?dataProperty ;
            owl:someValuesFrom ?datatype ] 
      ] .
  ?resource rdf:type ?class ;
    ?dataProperty ?value .
  ?dataProperty rdf:type owl:DatatypeProperty .
  FILTER(DATATYPE(?value)=?datatype)
}
```
**Explanation**

Since _resource_ is a _class_ which is equivalent to or a subclass of a class that has a complement of restriction on _dataProperty_ to have some values from _datatype_, _resource_ _dataProperty_ _value_, but _value_ has a datatype _datatype_, an inconsistency occurs.

**Example**
```
sio:hasValue rdf:type owl:DatatypeProperty ,
                                owl:FunctionalProperty;
    rdfs:label "has value" ;
    dct:description "A relation between a informational entity and its actual value (numeric, date, text, etc)." .

val:NumericalValue rdf:type owl:Class ;
    rdfs:label "numerical value" ;
    rdfs:subClassOf sio:ConceptualEntity ;
    rdfs:subClassOf
        [ rdf:type owl:Class ;
            owl:complementOf 
                [ rdf:type owl:Restriction ;
                    owl:onProperty sio:hasValue ;
                    owl:someValuesFrom xsd:string ] 
        ] .

val-kb:Number rdf:type val:NumericalValue ;
    sio:hasValue "Fifty"^^xsd:string .
```
A reasoner should infer `val-kb:Number rdf:type owl:Nothing .`
### Code
#### Deductor Agent
```python
class Deductor(GlobalChangeService):
    def __init__(self, reference, antecedent, consequent, explanation, resource="?resource", prefixes=None): 
        if resource is not None:
            self.resource = resource
        self.prefixes = {}
        if prefixes is not None:
            self.prefixes = prefixes
        self.reference = reference
        self.antecedent = antecedent
        self.consequent = consequent
        self.explanation = explanation

    def getInputClass(self):
        return pv.File

    def getOutputClass(self):
        return whyis.InferencedOver

    def get_query(self):
        self.app.db.store.nsBindings = {}
        return '''SELECT DISTINCT %s WHERE {\n%s \nFILTER NOT EXISTS {\n%s\n\t}\n}''' % (
        self.resource, self.antecedent, self.consequent)

    def get_context(self, i):
        context = {}
        context_vars = self.app.db.query('''SELECT DISTINCT * WHERE {\n%s \nFILTER(regex(str(%s), "^(%s)")) . }''' % (
        self.antecedent, self.resource, i.identifier), initNs=self.prefixes)
        for key in context_vars.vars :
            context[key] = context_vars.bindings[0][key]
        return context

    def process(self, i, o):
        for profile in self.app.config["active_profiles"] :
            if self.reference in self.app.config["reasoning_profiles"][profile] :
                npub = Nanopublication(store=o.graph.store)
                triples = self.app.db.query(
                    '''CONSTRUCT {\n%s\n} WHERE {\n%s \nFILTER NOT EXISTS {\n%s\n\t}\nFILTER (regex(str(%s), "^(%s)")) .\n}''' % (
                    self.consequent, self.antecedent, self.consequent, self.resource, i.identifier), initNs=self.prefixes)
                try :
                    for s, p, o in triples:
                        print("Deductor Adding ", s, p, o)
                        npub.assertion.add((s, p, o))
                except :
                    for s, p, o, c in triples:
                        print("Deductor Adding ", s, p, o)
                        npub.assertion.add((s, p, o))                
                npub.provenance.add((npub.assertion.identifier, prov.value,
                                     rdflib.Literal(flask.render_template_string(self.explanation, **self.get_context(i)))))
```
#### Backtracer Agent
```python
class BackTracer(GlobalChangeService):
    def __init__(self, reference, antecedent, consequent, explanation, resource="?resource", prefixes=None): 
        if resource is not None:
            self.resource = resource
        self.prefixes = {}
        if prefixes is not None:
            self.prefixes = prefixes
        self.reference = reference
        self.antecedent = antecedent
        self.consequent = consequent
        self.explanation = explanation

    def getInputClass(self):
        return pv.File
    def getOutputClass(self):
        return whyis.InferencedOver

    def get_query(self):
        self.app.db.store.nsBindings = {}
        return '''PREFIX whyis: <http://vocab.rpi.edu/whyis/> SELECT DISTINCT %s WHERE {\n%s GRAPH ?g { %s }\nFILTER NOT EXISTS {\n ?g whyis:hypothesis "%s" \n\t}\n}''' % (
        self.resource, self.antecedent, self.consequent, self.reference)

    def get_context(self, i):
        context = {}
        context_vars = self.app.db.query('''SELECT DISTINCT * WHERE {\n%s \nFILTER(regex(str(%s), "^(%s)")) . }''' % (
        self.antecedent, self.resource, i.identifier), initNs=self.prefixes)
        for key in context_vars.vars :
            context[key] = context_vars.bindings[0][key]
        return context

    def process(self, i, o):
        for profile in self.app.config["active_profiles"] :
            if self.reference in self.app.config["reasoning_profiles"][profile] :
                npub = Nanopublication(store=o.graph.store)
                triples = self.app.db.query(
                    '''PREFIX whyis: <http://vocab.rpi.edu/whyis/> CONSTRUCT {\n?g whyis:hypothesis "%s" . \n} WHERE {\n%s GRAPH ?g { %s } \nFILTER NOT EXISTS {\n?g whyis:hypothesis "%s" \n\t}\nFILTER (regex(str(%s), "^(%s)")) .\n}''' % (
                    self.reference, self.antecedent, self.consequent, self.reference, self.resource, i.identifier), initNs=self.prefixes)
                try :
                    for s, p, o in triples:
                        print("BackTracer Adding ", s, p, o)
                        npub.assertion.add((s, p, o))
                except :
                    for s, p, o, c in triples:
                        print("BackTracer Adding ", s, p, o)
                        npub.assertion.add((s, p, o))
```
### Support or Contact
Contact us at rashis2@rpi.edu.
