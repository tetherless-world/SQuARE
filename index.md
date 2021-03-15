# A Validation Ontology for Evaluating Semantic Reasoning Engines*
*This work is partially supported by IBM Research through the AI Horizons Network.

### Abstract
We describe an approach for building a deductive inference engine by encoding each OWL Description Logic (DL) axiom as a SPARQL CONSTRUCT query. While earlier work has proposed SPARQL extensions for various purposes, we find that the complete queries used in SPARQL-based reasoning methods are not publicly available. We were also unable to find a similar approach in the literature in which the OWL DL axioms are represented as SPARQL CONSTRUCT queries. We make openly available the queries, software, and the validation ontology that we use for our methodology. Encoded in this validation ontology are RDF examples for each OWL-DL axiom, allowing for the testing of our reasoning engine at a per axiom basis. We describe our approach in terms of implementation, query formulation, and validation. We evaluate the extent to which we are able to encode DL axioms and discuss the implications of the results. We further discuss future research directions that we are pursuing. The approach described in this paper has benefits related to inference engine customization capabilities and of being able to reason over inconsistent knowledge. This work is motivated by potential applications involving hybrid reasoning, distributed reasoning, and explainability in reasoning by embedding provenance in the form of nanopublications.

## Resources

### Ontology

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
```
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
val-kb:Farmer rdf:type sio:Role ;
    rdfs:label "farmer" .
```
#### Property Inclusion
**Axiom**

![formula](https://render.githubusercontent.com/render/math?math=P_1 \sqsubseteq P_2)
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

Any subject and object related by the property _p} is also related by _superProperty}. Therefore, since _resource_ _p} _o}, it is implied that _resource_ _superProperty} _o}.

**Example**

```
```
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

Any subject and object related by the property _p} is also related by _superProperty}. Therefore, since _resource_ _p} _o}, it is implied that _resource_ _superProperty} _o}.

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

Any subject and object related by the property _p} is also related by _superProperty}. Therefore, since _resource_ _p} _o}, it is implied that _resource_ _superProperty} _o}.

**Example**

```
valo:hasExactValue rdf:type owl:DatatypeProperty ;
    rdfs:label "has exact value" ;
    rdfs:subPropertyOf sio:hasValue .

val-kb:AgeOfSamantha valo:hasExactValue "25.82"^^xsd:decimal .
```

#### Object Property Chain Inclusion

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

### Code


## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/tetherless-world/validation/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/tetherless-world/validation/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
