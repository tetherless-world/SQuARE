# References
# w3.org/TR/owl2-syntax
# w3.org/TR/owl2-profiles

def get_rules() :
    InferenceRules = dict(
        Triple_Reference = { # eq-ref
            "reference" : "Triple Reference",
            "rule" : "sets:TripleReferenceRule",
            "resource" : "?s", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?s ?p ?o .''',
            "consequent" : "?s owl:sameAs ?s . ?p owl:sameAs ?p . ?o owl:sameAs ?o .",
            "explanation" : "All resources are the same as themselves."
        },
        Class_Disjointness = { # cax-dw  -- aligns with 9.1.3 Disjoint Classes
            "reference" : "Class Disjointness",
            "rule" : "sets:ClassDisjointnessRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x rdf:type ?c1 , ?c2 .
        { ?c1 owl:disjointWith ?c2 . } 
            UNION
        { ?c2 owl:disjointWith ?c1 . }''',
            "consequent" : "?x rdf:type owl:Nothing .",
            "explanation" : "Since {{c1}} is a disjoint with {{c2}}, any resource that is an instance of {{c1}} can't be an instance of {{c2}}. Therefore, since {{x}} is an instance of both {c1}} and {{c2}}, an inconsistency occurs."
        },
        Object_Property_Transitivity = { # addapted from prp-trp (to reference owl:ObjectProperty)-- aligns with 9.2.13
            "reference" : "Object Property Transitivity",
            "rule" : "sets:ObjectPropertyTransitivityRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        
        ?x ?p ?y .
        ?y  ?p ?z .
        ?p rdf:type owl:ObjectProperty , owl:TransitiveProperty .''',
            "consequent" : "?x ?p ?z .",
            "explanation" : "Since {{p}} is a transitive object property, and the relationships {{x}} {{p}} {{y}} and {{y}} {{p}} {{z}} exist, then we can infer that {{x}} {{p}} {{z}}."
        },
        Object_Property_Reflexivity_One = { # not supported by OWL-RL --- aligns with 9.2.9 Reflexive Object Properties -- but the example in the doc doesn't discuss domains -- should look into this further
            "reference" : "Object Property Reflexivity",
            "rule" : "sets:ObjectPropertyReflexivityTwoRule",
            "resource" : "?p", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        {
            ?x rdf:type owl:Individual .
        } UNION {
            ?x rdf:type/rdf:type owl:Class .
        }
        ?p rdf:type owl:ReflexiveProperty .
        FILTER NOT EXISTS (?p rdfs:domain ?c .)''',
            "consequent" : "?x ?p ?x .",
            "explanation" : "Since {{p}} is a reflexive property without a domain specified, for all individuals {{x}} in the ontology, we can infer that {{x}} {{p}} {{x}}."
        },
        Object_Property_Reflexivity_Two = { # not supported by OWL-RL
            "reference" : "Object Property Reflexivity Two",
            "rule" : "sets:ObjectPropertyReflexivityTwoRule",
            "resource" : "?p", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x rdf:type ?c .
        ?p rdf:type owl:ReflexiveProperty ;
            rdfs:domain ?c .''',
            "consequent" : "?x ?p ?x .",
            "explanation" : "Since {{p}} is a reflexive property with a domain specified, for all individuals {{x}} in that domain, we can infer that {{x}} {{p}} {{x}}."
        },
        Property_Domain_One = { # prp-dom  # note -- data and object property domains are both encoded with these sets of rules.. may want to separate out
            "reference" : "Property Domain One",
            "rule" : "sets:PropertyDomainOneRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x ?p ?y .
        ?p rdfs:domain ?c .''',
            "consequent" : "?x rdf:type ?c .",
            "explanation" : "Since the domain of {{p}} is {{c}}, and we have the triple {{x}} {{p}} {{y}}, this implies that {{x}} is a {{c}}."
        },
        Property_Domain_Two = { # scm-dom1
            "reference" : "Property Domain Two",
            "rule" : "sets:PropertyDomainTwoRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?p rdfs:domain ?c1 .
        ?c1 rdfs:subClassOf+ ?c2''',
            "consequent" : "?p rdfs:domain ?c .",
            "explanation" : "Since the domain of {{p}} is {{c1}}, and {{c1}} is a subclass of {{c2}}, this implies that the domain of {{p}} is also {{c2}}."
        },
        Property_Domain_Three = { # scm-dom2
            "reference" : "Property Domain Three",
            "rule" : "sets:PropertyDomainThreeRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?p2 rdfs:domain ?c .
        ?p1 rdfs:subPropertyOf ?p2''',
            "consequent" : "?p1 rdfs:domain ?c .",
            "explanation" : "Since the domain of {{p2}} is {{c}}, and {{p1}} is a subproperty of {{p2}}, this implies that the domain of {{p1}} is also {{c}}."
        },
        Property_Range_One = { # prp-rng  # note -- data and object property ranges are both encoded with these sets of rules.. may want to separate out
            "reference" : "Property Range One",
            "rule" : "sets:PropertyRangeOneRule",
            "resource" : "?resource",
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdfs:range ?class .''',
            "consequent" : "?o rdf:type ?class .",
            "explanation" : "Since the range of {{p}} is {{class}}, this implies that {{o}} is a {{class}}."
        },
        Property_Range_Two = { # scm-rng1
            "reference" : "Property Range Two",
            "rule" : "sets:PropertyRangeTwoRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?p rdfs:range ?c1 .
        ?c1 rdfs:subClassOf+ ?c2''',
            "consequent" : "?p rdfs:range ?c .",
            "explanation" : "Since the range of {{p}} is {{c1}}, and {{c1}} is a subclass of {{c2}}, this implies that the range of {{p}} is also {{c2}}."
        },
        Property_Range_Three = { # scm-rng2
            "reference" : "Property Range Three",
            "rule" : "sets:PropertyRangeThreeRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?p2 rdfs:range ?c .
        ?p1 rdfs:subPropertyOf ?p2''',
            "consequent" : "?p1 rdfs:range ?c .",
            "explanation" : "Since the range of {{p2}} is {{c}}, and {{p1}} is a subproperty of {{p2}}, this implies that the range of {{p1}} is also {{c}}."
        },
        Functional_Data_Property = { # in line with 9.3.6 Function Data Properties
            "reference" : "Functional Data Property",
            "rule" : "sets:FunctionalDataPropertyRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x ?p ?y1 , ?y2 .
        ?p rdf:type owl:DatatypeProperty ,
                owl:FunctionalProperty .
        FILTER (str(?y1) !=  str(?y2))''',
            "consequent" : "?x rdf:type owl:Nothing .",
            "explanation" : "Since {{p}} is a functional data property, {{x}} can only have one value for {{p}}. Since {{x}} {{p}} both {{y1}} and {{y2}}, and {{y1}} is different from {{y2}}, an inconsistency occurs."
        },
        Functional_Object_Property = { # prp-fp --- aligns with 9.2.7 Functional Object Properties
            "reference" : "Functional Object Property",
            "rule" : "sets:FunctionalObjectPropertyRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x ?p ?y1 , ?y2 .
        ?p rdf:type owl:ObjectProperty , 
                owl:FunctionalProperty .
        FILTER (str( ?y1 ) !=  str( ?y2 ))''',
            "consequent" : "?y1 owl:sameAs ?y2 .",
            "explanation" : "Since {{p}} is a functional object property, {{x}} can only have one value for {{p}}. Since {{x}} {{p}} both {{y1}} and {{y2}}, we can infer that {{y1}} and {{y2}} must be the same individual."
        },
        Object_Property_Disjointness = { # adapted from prp-pdw (to include reference to ObjectProperty) .. also in line with 9.2.3 Disjoint Object Properties -- however, 9.2.3 alludes to the ability to define a list of properties that are all disjoint with eachother . Nevertheless, this is supported with the AllDisjointProperties rule
            "reference" : "Object Property Disjointness",
            "rule" : "sets:ObjectPropertyDisjointnessRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x ?p1 ?y .
        ?x ?p2 ?y .
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        {?p1 owl:propertyDisjointWith ?p2 .}
            UNION
        {?p2 owl:propertyDisjointWith ?p1 .}''',
            "consequent" : "?x rdf:type owl:Nothing .",
            "explanation" : "Since properties {p1} and {p2} are disjoint, {{x}} having both {{p2}} {{y}} as well as {{p1}} {{y}} leads to an inconsistency. "
        },
        Data_Property_Disjointness = { # adapted from prp-pdw (to include reference to DataProperty) -- also in line with 9.3.3 Disjoint Data Properties
            "reference" : "Data Property Disjointness",
            "rule" : "sets:DataPropertyDisjointnessRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x ?p1 ?y .
        ?x ?p2 ?y .
        ?p1 rdf:type owl:DatatypeProperty .
        ?p2 rdf:type owl:DatatypeProperty .
        {?p1 owl:propertyDisjointWith ?p2 .}
            UNION
        {?p2 owl:propertyDisjointWith ?p1 .}''',
            "consequent" : "?x rdf:type owl:Nothing .",
            "explanation" : "Since properties {p1} and {p2} are disjoint, {{x}} having both {{p2}} {{y}} as well as {{p1}} {{y}} leads to an inconsistency. "
        },
        Object_Property_Asymmetry = { # prp-asyp -- aligned with 9.2.12 Assymetric Object Properties
            "reference" : "Object Property Asymmetry",
            "rule" : "sets:ObjectPropertyAsymmetryRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?asymmetricProperty ?o .
        ?asymmetricProperty rdf:type owl:AsymmetricProperty .
        ?o ?asymmetricProperty ?resource .''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{asymmetricProperty}} is an asymmetric property, and {{resource}} {{asymmetricProperty}} {{o}}, then the assertion {{o}} {{asymmetricProperty}} {{resource}} results in an inconsistency."
        },
        Object_Property_Symmetry = { # prp-symp -- aligns with 9.2.11 Symmetric object property
            "reference" : "Object Property Symmetry",
            "rule" : "sets:ObjectPropertySymmetryRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?symmetricProperty ?o .
        ?symmetricProperty rdf:type owl:SymmetricProperty .''',
            "consequent" : "?o ?symmetricProperty ?resource .",
            "explanation" : "Since {{symmetricProperty}} is a symmetric property, and {{resource}} {{symmetricProperty}} {{o}}, we can infer that {{o}} {{symmetricProperty}} {{resource}}."
        },
        Object_Property_Irreflexivity = { # prp-irp -- aligns with 9.2.10 Irreflexive Object Properties
            "reference" : "Object Property Irreflexivity",
            "rule" : "sets:ObjectPropertyIrreflexivityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?irreflexiveProperty ?o .
        ?irreflexiveProperty rdf:type owl:IrreflexiveProperty .
        ?resource ?irreflexiveProperty ?resource .''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{resource}} has a {{irreflexiveProperty}} assertion, and {{irreflexiveProperty}} is a irreflexive property, we can infer that the relationship {{resource}} {{irreflexiveProperty}} {{resource}} does not exist."
        },
        Class_Assertion = { # scm-cls
            "reference" : "Class Assertion",
            "rule" : "sets:ClassAssertionRule",
            "resource" : "?c", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c rdf:type owl:Class.''',
            "consequent" : "?c rdfs:subClassOf ?c , owl:Thing ; owl:equivalentClass ?c . owl:Nothing rdfs:subClassOf ?c .",
            "explanation" : "Since {{c}} is a class, it is a subclass of itself and owl:Thing and is equivalent to itself. Furthermore, owl:Nothing is a subclass of {{c}}."
        },
        Class_Inclusion = { # scm-sco   -- aligns with 9.1.1 SubClass Axioms
            "reference" : "Class Inclusion",
            "rule" : "sets:ClassInclusionRule",
            "resource" : "?c1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c1 rdfs:subClassOf ?c2 .
        ?c2 rdfs:subClassOf+ ?c3 .''',
            "consequent" : "?c1 rdfs:subClassOf ?c3 .",
            "explanation" : "Since {{c2}} is a subclass of {{c3}}, any class that is a subclass of {{c2}} is also a subclass of {{c3}}. Therefore, {{c1}} is a subclass of {{c3}}."
        },
        Individual_Inclusion = { # cax-sco
            "reference" : "Individual Inclusion",
            "rule" : "sets:IndividualInclusionRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x rdf:type ?c1 .
        ?c1 rdfs:subClassOf+ ?c2 .''',
            "consequent" : "?x rdf:type ?c2 .",
            "explanation" : "Since {{c1}} is a subclass of {{c2}}, any individual that is an instance of {{c1}} is also an instance of {{c2}}. Therefore, {{x}} is an instance of {{c2}}."
        },
        Object_Property_Inclusion_One = { # prp-spo1 -- aligns with 9.2.1 Object Subproperties
            "reference" : "Object Property Inclusion One",
            "rule" : "sets:ObjectPropertyInclusionOneRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdf:type owl:ObjectProperty ;
            rdfs:subPropertyOf+ ?superProperty .''',
            "consequent" : "?resource ?superProperty ?o .",
            "explanation" : "Any subject and object related by the property {{p}} is also related by {{superProperty}}. Therefore, since {{resource}} {{p}} {{o}}, it is implied that {{resource}} {{superProperty}} {{o}}."
        },
        Object_Property_Inclusion_Two = { # scm-spo
            "reference" : "Object Property Inclusion Two",
            "rule" : "sets:ObjectPropertyInclusionTwoRule",
            "resource" : "?p1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        ?p3 rdf:type owl:ObjectProperty .
        ?p1 rdfs:subPropertyOf ?p2 .
        ?p2 rdfs:subPropertyOf+ ?p3 .''',
            "consequent" : "?p1 rdfs:subPropertyOf ?p3 .",
            "explanation" : "Since {{p2}} is a subproperty of {{p3}}, any class that is a subproperty of {{p2}} is also a subproperty of {{p3}}. Therefore, {{p1}} is a subproperty of {{p3}}."
        },
        Data_Property_Inclusion_One = { # prp-spo1  -- also in line with 9.3.1 Data Subproperties
            "reference" : "Data Property Inclusion One",
            "rule" : "sets:DataPropertyInclusionOneRule",
            "resource" : "?resource",
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdf:type owl:DatatypeProperty ;
            rdfs:subPropertyOf+ ?superProperty .''',
            "consequent" : "?resource ?superProperty ?o .",
            "explanation" : "Any subject and object related by the property {{p}} is also related by {{superProperty}}. Therefore, since {{resource}} {{p}} {{o}}, it is implied that {{resource}} {{superProperty}} {{o}}."
        },
        Data_Property_Inclusion_Two = { # scm-spo
            "reference" : "Data Property Inclusion Two",
            "rule" : "sets:DataPropertyInclusionTwoRule",
            "resource" : "?p1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?p1 rdf:type owl:DatatypeProperty .
        ?p2 rdf:type owl:DatatypeProperty .
        ?p3 rdf:type owl:DatatypeProperty .
        ?p1 rdfs:subPropertyOf ?p2 .
        ?p2 rdfs:subPropertyOf+ ?p3 .''',
            "consequent" : "?p1 rdfs:subPropertyOf ?p3 .",
            "explanation" : "Since {{p2}} is a subproperty of {{p3}}, any class that is a subproperty of {{p2}} is also a subproperty of {{p3}}. Therefore, {{p1}} is a subproperty of {{p3}}."
        },
        Class_Equivalence_One = { # cax-eqc1  -- somewhat aligns with 9.1.2 Equivalent Classes -- in those examples they use value restrictions
            "reference" : "Class Equivalence One",
            "rule" : "sets:ClassEquivalenceOneRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x rdf:type ?c1 .
        {?c1 owl:equivalentClass ?c2 .}
            UNION
        {?c2 owl:equivalentClass ?c1 .}''', 
            "consequent" : "?x rdf:type ?c2 .",
            "explanation" : "{{c1}} is equivalent to {{c2}}, so since {{x}} is a {{c1}}, it is also a {{c2}}."
        },
        Class_Equivalence_Two = { # cax-eqc2  -- this rule may be redundant -- should check
            "reference" : "Class Equivalence Two",
            "rule" : "sets:ClassEquivalenceTwoRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x rdf:type ?c2 .
        {?c1 owl:equivalentClass ?c2 .}
            UNION
        {?c2 owl:equivalentClass ?c1 .}''', 
            "consequent" : "?x rdf:type ?c1 .",
            "explanation" : "{{c1}} is equivalent to {{c2}}, so since {{x}} is a {{c2}}, it is also a {{c1}}."
        },
        Class_Equivalence_Three = { # cax-eqc1 -- aligns with 9.1.2 Equivalent Classes
            "reference" : "Class Equivalence Three",
            "rule" : "sets:ClassEquivalenceThreeRule",
            "resource" : "?c1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        {?c1 owl:equivalentClass ?c2 .}
            UNION
        {?c2 owl:equivalentClass ?c1 .}''', 
            "consequent" : "?c1 rdfs:subClassOf ?c2 . ?c2 rdfs:subClassOf ?c1 .",
            "explanation" : "Since {{c1}} and {{c2}} are equivalent classes, they are both subclasses of eachother."
        },
        Class_Equivalence_Four = { # cax-eqc2
            "reference" : "Class Equivalence Four",
            "rule" : "sets:ClassEquivalenceFourRule",
            "resource" : "?c1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?c1 rdfs:subClassOf ?c2 .
        ?c2 rdfs:subClassOf ?c1 .''',
            "consequent" : "?c1 owl:equivalentClass ?c2 .",
            "explanation" : "Since {{c1}} and {{c2}} are both subclasses of eachother, they are equivalent classes."
        },
        Object_Property_Equivalence_One = { # prp-eqp1 -- aligns with 9.2.2 Equivalent Object Properties
            "reference" : "Object Property Equivalence One",
            "rule" : "sets:ObjectPropertyEquivalenceOneRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x ?p1 ?y .
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        {?p1 owl:equivalentProperty ?p2 .}
            UNION
        {?p2 owl:equivalentProperty ?p1 . }''', 
            "consequent" : "?x ?p2 ?y .",
            "explanation" : "The properties {{p1}} and {{p2}} are equivalent. Therefore, since {{x} {{p1}} {{y}}, it is implied that {{x}} {{p2}} {{y}}."
        },
        Object_Property_Equivalence_Two = { # prp-eqp2
            "reference" : "Object Property Equivalence Two",
            "rule" : "sets:ObjectPropertyEquivalenceTwoRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x ?p2 ?y .
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        {?p1 owl:equivalentProperty ?p2 .}
            UNION
        {?p2 owl:equivalentProperty ?p1 . }''', 
            "consequent" : "?x ?p1 ?y .",
            "explanation" : "The properties {{p1}} and {{p2}} are equivalent. Therefore, since {{x} {{p2}} {{y}}, it is implied that {{x}} {{p1}} {{y}}."
        },
        Object_Property_Equivalence_Three = { # scm-eqp1  -- aligns with 9.2.2 Equivalent Object Properties
            "reference" : "Object Property Equivalence Three",
            "rule" : "sets:ObjectPropertyEquivalenceThreeRule",
            "resource" : "?p1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        {?p1 owl:equivalentProperty ?p2 .}
            UNION
        {?p2 owl:equivalentProperty ?p1 .}''', 
            "consequent" : "?p1 rdfs:subPropertyOf ?p2 . ?p2 rdfs:subPropertyOf ?p1 .",
            "explanation" : "Since {{p1}} and {{p2}} are equivalent properties, they are both subproperties of eachother."
        },
        Object_Property_Equivalence_Four = { # scm-eqp2
            "reference" : "Object Property Equivalence Four",
            "rule" : "sets:ObjectPropertyEquivalenceFourRule",
            "resource" : "?p1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        ?p1 rdfs:subPropertyOf ?p2 .
        ?p2 rdfs:subPropertyOf ?p1 .''',
            "consequent" : "?p1 owl:equivalentProperty ?p2 .",
            "explanation" : "Since {{p1}} and {{p2}} are both subproperties of eachother, they are equivalent properties."
        },
        Data_Property_Equivalence_One = { # prp-eqp1 -- also in line with 9.3.2 Equivalent Data Properties
            "reference" : "Data Property Equivalence One",
            "rule" : "sets:DataPropertyEquivalenceOneRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x ?p1 ?y .
        ?p1 rdf:type owl:DatatypeProperty .
        ?p2 rdf:type owl:DatatypeProperty .
        {?p1 owl:equivalentProperty ?p2 .}
            UNION
        {?p2 owl:equivalentProperty ?p1 . }''', 
            "consequent" : "?x ?p2 ?y .",
            "explanation" : "The properties {{p1}} and {{p2}} are equivalent. Therefore, since {{x} {{p1}} {{y}}, it is implied that {{x}} {{p2}} {{y}}."
        },
        Data_Property_Equivalence_Two = { # prp-eqp2  -- This rule might be redundant. Should test to confirm
            "reference" : "Data Property Equivalence Two",
            "rule" : "sets:DataPropertyEquivalenceTwoRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x ?p2 ?y .
        ?p1 rdf:type owl:DatatypeProperty .
        ?p2 rdf:type owl:DatatypeProperty .
        {?p1 owl:equivalentProperty ?p2 .}
            UNION
        {?p2 owl:equivalentProperty ?p1 . }''', 
            "consequent" : "?x ?p1 ?y .",
            "explanation" : "The properties {{p1}} and {{p2}} are equivalent. Therefore, since {{x} {{p2}} {{y}}, it is implied that {{x}} {{p1}} {{y}}."
        },
        Data_Property_Equivalence_Three = { # scm-eqp1
            "reference" : "Data Property Equivalence Three",
            "rule" : "sets:DataPropertyEquivalenceThreeRule",
            "resource" : "?p1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p1 rdf:type owl:DatatypeProperty .
        ?p2 rdf:type owl:DatatypeProperty .
        {?p1 owl:equivalentProperty ?p2 .}
            UNION
        {?p2 owl:equivalentProperty ?p1 .}''', 
            "consequent" : "?p1 rdfs:subPropertyOf ?p2 . ?p2 rdfs:subPropertyOf ?p1 .",
            "explanation" : "Since {{p1}} and {{p2}} are equivalent properties, they are both subproperties of eachother."
        },
        Data_Property_Equivalence_Four = { # scm-eqp2
            "reference" : "Data Property Equivalence Four",
            "rule" : "sets:DataPropertyEquivalenceFourRule",
            "resource" : "?p1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p1 rdf:type owl:DatatypeProperty .
        ?p2 rdf:type owl:DatatypeProperty .
        ?p1 rdfs:subPropertyOf ?p2 .
        ?p2 rdfs:subPropertyOf ?p1 .''',
            "consequent" : "?p1 owl:equivalentProperty ?p2 .",
            "explanation" : "Since {{p1}} and {{p2}} are both subproperties of eachother, they are equivalent properties."
        },
        Object_Property_Inversion_One = { # prp-inv-1 - in line with 6.1.1 Inverse Object Properties and 9.2.4 Inverse Object Properties
            "reference" : "Object Property Inversion One",
            "rule" : "sets:ObjectPropertyInversionOneRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x ?p1 ?y .
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        {?p1 owl:inverseOf ?p2 .}
            UNION
        {?p2 owl:inverseOf ?p1 .}''', 
            "consequent" : "?y ?p2 ?x .",
            "explanation" : "The object properties {{p1}} and {{p2}} are inversely related to eachother. Therefore, since {{x}} {{p1}} {{y}}, it is implied that {{y}} {{p2}} {{x}}."
        },
        Object_Property_Inversion_Two = { # prp-inv-2 # this rule may be redundant, should test
            "reference" : "Object Property Inversion One",
            "rule" : "sets:ObjectPropertyInversionOneRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x ?p2 ?y .
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        {?p1 owl:inverseOf ?p2 .}
            UNION
        {?p2 owl:inverseOf ?p1 .}''', 
            "consequent" : "?y ?p1 ?x .",
            "explanation" : "The object properties {{p1}} and {{p2}} are inversely related to eachother. Therefore, since {{x}} {{p2}} {{y}}, it is implied that {{y}} {{p1}} {{x}}."
        },
        Same_As_Symmetry = { #eq-sym
            "reference" : "Same As Symmetry",
            "rule" : "sets:SameAsSymmetry",
            "resource" : "?y", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x owl:sameAs ?y .''', 
            "consequent" : "?y owl:sameAs ?x .",
            "explanation" : "Since {{x}} is the same as {{y}}, {{y}} is the same as {{x}}."
        },
        Same_As_Transitivity = { #eq-trans
            "reference" : "Same As Transitivity",
            "rule" : "sets:SameAsTransitivity",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?x owl:sameAs ?y . ?y owl:sameAs ?z .''', 
            "consequent" : "?x owl:sameAs ?z .",
            "explanation" : "Since {{x}} is the same as {{y}} and {{y}} same as {{z}, {{x}} is the same as {{z}}."
        },
        Same_Subject = { # eq-rep-s
            "reference" : "Same Subject",
            "rule" : "sets:SameSubjectRule",
            "resource" : "?sp", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?s owl:sameAs ?sp .
        ?s ?p ?o .''', 
            "consequent" : "?sp ?p ?o .",
            "explanation" : "Since {{s}} is the same as {{sp}}, they share the same properties."#except maybe for annotation properties? should possibly add this check in
        },
        Same_Property = { # eq-rep-p
            "reference" : "Same Property",
            "rule" : "sets:SamePropertyRule",
            "resource" : "?pp", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p owl:sameAs ?pp .
        ?s ?p ?o .''', 
            "consequent" : "?s ?pp ?o .",
            "explanation" : "Since {{p}} is the same as {{pp}}, they link the same subject and objects."#except maybe for annotation properties? should possibly add this check in
        },
        Same_Object = { # eq-rep-o
            "reference" : "Same Object",
            "rule" : "sets:SameObjectRule",
            "resource" : "?op", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?o owl:sameAs ?op .
        ?s ?p ?o .''', 
            "consequent" : "?s ?p ?op .",
            "explanation" : "Since {{o}} is the same as {{op}}, they share the same subject predicate links."#except maybe for annotation properties? should possibly add this check in
        },
        Different_Individuals = { # eq-diff-1
            "reference" : "Different Individuals",
            "rule" : "sets:DifferentIndividualsRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        {
            ?resource owl:differentFrom ?individual .
        }
            UNION
        {
            ?individual owl:differentFrom ?resource .
        }
        ?resource owl:sameAs ?individual .''', 
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{resource}} is asserted as being different from {{individual}}, the assertion that {{resource}} is the same as {{individual}} leads to an inconsistency."
        },
        All_Different_Individuals = { # eq-diff-2 and # eq-diff-3
            "reference" : "All Different Individuals",
            "rule" : "sets:AllDifferentIndividualsRule",
            "resource" : "?restriction", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?restriction rdf:type owl:AllDifferent ;
            owl:distinctMembers|owl:members ?list .
        ?list rdf:rest*/rdf:first ?member .
        {
            SELECT DISTINCT ?item ?restrict WHERE
            {
                ?restrict rdf:type owl:AllDifferent ;
                    owl:distinctMembers|owl:members ?list .
                ?list rdf:rest*/rdf:first ?item .
            }
        }
        BIND( ?restriction AS ?restrict ) 
        FILTER( ?member != ?item )''', 
            "consequent" : "?member owl:differentFrom ?item .",
            "explanation" : "Since {{restriction}} is an all different restriction with individuals listed in {{list}}, each member in {{list}} is different from each other member in the list."
        },
        Positive_Object_Property_Assertion = { # This is essentially just the ability to use object properties, so doesn't necessarily need a rule -- our implementation also assets the object of a triple that includes an object property is an individual
            "reference" : "Positive Object Property Assertion",
            "rule" : "sets:PositiveObjectPropertyAssertionRule",
            "resource" : "?o", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p rdf:type owl:ObjectProperty .
        ?s ?p ?o.''',
            "consequent" : "?o rdf:type owl:Individual .",
            "explanation" : "Since {{p}} is defined to be an object property, {{o}} must be an individual ."
        },
        Positive_Data_Property_Assertion = { # This is essentially just the ability to use datatype properties, so doesn't necessarily need a rule -- our implementation also assets the object of a triple that includes a datatype property is a literal
            "reference" : "Positive Data Property Assertion",
            "rule" : "sets:PositiveDataPropertyAssertionRule",
            "resource" : "?o", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p rdf:type owl:DatatypeProperty .
        ?s ?p ?o.''',
            "consequent" : "?o rdf:type rdfs:Literal .",
            "explanation" : "Since {{p}} is defined to be a data property, {{o}} must be a literal."
        },
        Object_Property_Definition = { # scm-op
            "reference" : "Object Property Definition",
            "rule" : "sets:ObjectPropertyDefinitionRule",
            "resource" : "?p", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p rdf:type owl:ObjectProperty .''',
            "consequent" : "?p rdfs:subPropertyOf ?p ; owl:equivalentProperty ?p .",
            "explanation" : "Since {{p}} is defined to be an object property, it is a subproperty of and equivalent to itself."
        },
        Data_Property_Definition = { # scm-dp
            "reference" : "Data Property Definition",
            "rule" : "sets:DataPropertyDefinitionRule",
            "resource" : "?p", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?p rdf:type owl:DatatypeProperty .''',
            "consequent" : "?p rdfs:subPropertyOf ?p ; owl:equivalentProperty ?p .",
            "explanation" : "Since {{p}} is defined to be a data property, it is a subproperty of and equivalent to itself."
        },
        Negative_Object_Property_Assertion = { # prp-npa1 
            "reference" : "Negative Object Property Assertion",
            "rule" : "sets:NegativeObjectPropertyAssertionRule",
            "resource" : "?i1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?i1 ?p ?i2 .
        ?p rdf:type owl:ObjectProperty .
        ?x rdf:type owl:NegativePropertyAssertion ;
            owl:sourceIndividual ?i1 ;
            owl:assertionProperty ?p ;
            owl:targetIndividual ?i2 .''', 
            "consequent" : "?i1 rdf:type owl:Nothing .",
            "explanation" : "Since a negative object property assertion was made with source {{i1}}, object property {{p}}, and target individual {{i2}}, the existence of {{i1}} {{p}} {{i2}} results in an inconsistency."
        },
        Negative_Data_Property_Assertion = { # prp-npa2
            "reference" : "Negative Data Property Assertion",
            "rule" : "sets:NegativeDataPropertyAssertionRule",
            "resource" : "?i", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?i ?p ?lt .
        ?p rdf:type owl:DatatypeProperty .
        ?x rdf:type owl:NegativePropertyAssertion ;
            owl:sourceIndividual ?i ;
            owl:assertionProperty ?p ;
            owl:targetValue ?lt .''', 
            "consequent" : "?i rdf:type owl:Nothing .",
            "explanation" : "Since a negative datatype property assertion was made with source {{i}}, datatype property {{p}}, and target value {{lt}}, the existence of {{i}} {{p}} {{lt}} results in an inconsistency."
        },
        Single_Key = { # prp-key -- note in 9.5 datatype key properties are discussed -- may need to encode some of those rules
            "reference" : "Single Key",
            "rule" : "sets:SingleKeyRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x rdf:type ?c ;
            ?keyProperty ?keyValue .
        ?c rdf:type owl:Class ;
            owl:hasKey ( ?keyProperty ) .
        ?y rdf:type ?c ;
            ?keyProperty ?keyValue .''',
            "consequent" : "?x owl:sameAs ?y .",
            "explanation" : "Since {{c}} has key {{keyProperty}}, {{x}} and {{y}} are both of type {{c}}, and {{x}} and {{y}} both {{keyProperty}} {{keyValue}}, then {{x}} and {{y}} must be the same."
        },
        Multiple_Keys = { # prp-key -- prob not correct
            "reference" : "Multiple Keys",
            "rule" : "sets:MultipleKeysRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c owl:hasKey ?u .
        ?u rdf:rest*/rdf:first ?pi .
        ?x rdf:type ?c .
        ?x ?pi ?z .
        ?y ?pi ?z .
        ?y rdf:type ?c .''',
            "consequent" : "?x owl:sameAs ?y .",
            "explanation" : "Since {{c}} has key {{keyProperty}}, {{x}} and {{y}} are both of type {{c}}, and {{x}} and {{y}} both {{keyProperty}} {{keyValue}}, then {{x}} and {{y}} must be the same."
        },
        Inverse_Functional_Object_Property = { # prp-ifp --- aligns with 9.2.8 Inverse-Functional Object Properties
            "reference" : "Inverse Functional Object Property",
            "rule" : "sets:InverseFunctionalObjectPropertyRule",
            "resource" : "?x1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x1 ?p ?o .
        ?x2 ?p ?o .
        ?p rdf:type owl:ObjectProperty ,
                owl:InverseFunctionalProperty .''',
            "consequent" : "?x1 owl:sameAs ?x2",
            "explanation" : "Since {{p}} is an inverse functional property, and {{x1}} and {{x2}} both have the relationship {{p}} {{o}}, then we can infer that {{x1}} is the same as {{x2}}."
        },
        Object_Some_Values_From_One = {# cls-svf1 , cls-svf2 -- in line with 8.2.1 Existential Quantification
            "reference" : "Object Some Values From One",
            "rule" : "sets:ObjectSomeValuesFromOneRule",
            "resource" : "?u", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?u ?p ?v .
        ?p rdf:type owl:ObjectProperty .
        {
            ?x (owl:equivalentClass*|rdfs:subClassOf*)/owl:someValuesFrom ?y ;
                (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p .
            ?v rdf:type ?y
        } UNION {
            ?x (owl:equivalentClass*|rdfs:subClassOf*)/owl:someValuesFrom owl:Thing ;
                (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p .
        }''',
            "consequent" : "?u rdf:type ?x .",
            "explanation" : "Since {{u}} {{p}} {{v}}, and there is either a some values from restriction on {{p}} to have values from owl:Thing or from {{y}} with {{v}} being of type {{y}}, we can infer {{u}} is of the {{x}}."
        },
        Object_Some_Values_From_Two = {# scm-svf1
            "reference" : "Object Some Values From Two",
            "rule" : "sets:ObjectSomeValuesFromTwoRule",
            "resource" : "?c1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?p rdf:type owl:ObjectProperty .
        ?c1 (owl:equivalentClass*|rdfs:subClassOf*)/owl:someValuesFrom ?y1 ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p .
        ?c2 (owl:equivalentClass*|rdfs:subClassOf*)/owl:someValuesFrom ?y2 ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p .
        ?y1 rdfs:subClassOf ?y2 .''',
            "consequent" : "?c1 rdfs:subClassOf ?c2 .",
            "explanation" : ""
        },
        Object_Some_Values_From_Three = {# scm-svf2
            "reference" : "Object Some Values From Three",
            "rule" : "sets:ObjectSomeValuesFromThreeRule",
            "resource" : "?c1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?p1 rdf:type owl:ObjectProperty .
        ?p2 rdf:type owl:ObjectProperty .
        ?c1 (owl:equivalentClass*|rdfs:subClassOf*)/owl:someValuesFrom ?y ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p1 .
        ?c2 (owl:equivalentClass*|rdfs:subClassOf*)/owl:someValuesFrom ?y ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p2 .
        ?p1 rdfs:subPropertyOf ?p2 .''',
            "consequent" : "?c1 rdfs:subClassOf ?c2 .",
            "explanation" : ""
        },
        Data_Some_Values_From = { # Not quite in line with 8.4.1 Existential Quantification -- should revisit
            "reference" : "Data Some Values From",
            "rule" : "sets:DataSomeValuesFromRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?datatypeProperty ?val .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?class (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?datatypeProperty ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:someValuesFrom ?value .
        FILTER( DATATYPE( ?val ) != ?value )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "{{resource}} {{datatypeProperty}} {{val}}, but {{val}} does not the same datatype {{value}} restricted for {{datatypeProperty}} in {{class}}. Since {{resource}} rdf:type {{class}}, an inconsistency occurs."
        },#Data some and all values from behave the same as each other..? May need to revisit
        Object_Has_Self_One = { # not included in the document .. is this included in RL? included in profile but should confirm
            "reference" : "Object Has Self One", 
            "rule" : "sets:ObjectHasSelfOneRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?objectProperty ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:hasSelf \"true\"^^xsd:boolean .''',
            "consequent" : "?resource ?objectProperty ?resource .",
            "explanation" : "{{resource}} is of type {{class}}, which has a self restriction on the property {{objectProperty}}, allowing us to infer {{resource}} {{objectProperty}} {{resource}}."
        },
        Object_Has_Self = { # aligns with 8.2.4 Self-Restriction
            "reference" : "Object Has Self Two", 
            "rule" : "sets:ObjectHasSelfTwoRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?objectProperty ?resource
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?objectProperty ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:hasSelf \"true\"^^xsd:boolean .''',
            "consequent" : "?resource rdf:type ?class .",
            "explanation" : "{{resource}} {{objectProperty}} {{resource}} and {{class}} has a self restriction on the property {{objectProperty}}, allowing us to infer {{resource}} is of type {{class}}."
        },
        Object_Has_Value_One = { # cls-hv1
            "reference" : "Object Has Value One",
            "rule" : "sets:ObjectHasValueOneRule",
            "resource" : "?u",
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?u rdf:type ?x .
        ?p rdf:type owl:ObjectProperty.
        ?x (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p ;
           (owl:equivalentClass*|rdfs:subClassOf*)/owl:hasValue ?y .''',
            "consequent" : "?u ?p ?y .",
            "explanation" : "Since {{u}} is of type {{x}}, which has a value restriction on {{p}} to have value {{y}}, we can infer that {{u}} {{p}} {{y}}."
        },
        Object_Has_Value_Two = { # cls-hv2 -- in line with 8.2.3 Individual value restriction
            "reference" : "Object Has Value Two",
            "rule" : "sets:ObjectHasValueTwoRule",
            "resource" : "?u",
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?u ?p ?y .
        ?p rdf:type owl:ObjectProperty.
        ?x (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p ;
           (owl:equivalentClass*|rdfs:subClassOf*)/owl:hasValue ?y .''',
            "consequent" : "?u rdf:type ?x .",
            "explanation" : "Since {{u}} {{p}} {{y}}, we can infer that {{u}} is of type {{x}}, since {{x}} has a value restriction on {{p}} to have value {{y}}."
        },
        Property_Has_Value = { # scm-hv
            "reference" : "Property Has Value",
            "rule" : "sets:PropertyHasValueRule",
            "resource" : "?c1",
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c1 owl:hasValue ?i ;
            owl:onProperty ?p1 .
        ?c2 owl:hasValue ?i ;
            owl:onProperty ?p2 .
        ?p1 rdfs:subPropertyOf ?p2 .''',
            "consequent" : "?c1 rdfs:subClassOf ?c2 .",
            "explanation" : "Since {{c1}} has a value restriction of {{i}} on property {{p1}} and {{c2}} has a value restriction of {{i}} on property {{p2}}, and {{p1}} is a subproperty of {{p2}}, we can infer that {{c1}} is a subclass of {{c2}}."
        },
        Data_Has_Value = { #  aligns with 8.4.3 Literal Value Restriction but still should look into this further -- Note that only owl:equivalentClass results in inference, not rdfs:subClassOf -- need to understand why
            "reference" : "Data Has Value",
            "rule" : "sets:DataHasValueRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?datatypeProperty ?value .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?class owl:equivalentClass*/owl:onProperty ?datatypeProperty ;
            owl:equivalentClass*/owl:hasValue ?value .''',
            "consequent" : "?resource rdf:type ?class .",
            "explanation" : "Since {{class}} is equivalent to the restriction on {{datatypeProperty}} to have value {{value}} and {{resource}} {{datatypeProperty}} {{value}}, we can infer that {{resource}} rdf:type {{class}}."
        },
        Object_One_Of_Membership = { # cls-oo -- note this is not quite the same as 8.1.4 Enumeration of Individuals
            "reference" : "Object One Of Membership",
            "rule" : "sets:ObjectOneOfMembershipRule",
            "resource" : "?c", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c rdf:type owl:Class ;
            owl:oneOf ?x .
        ?x rdf:rest*/rdf:first ?yi .''',
            "consequent" : "?yi rdf:type ?c .",
            "explanation" : "Since {{c}} has a one of relationship with {{x}}, the member {{yi}} in {{x}} is of type {{c}}."
        },
        Object_One_Of_Inconsistency = { # is this encoded somewhere? is this necessary? some thinking to do
            "reference" : "Object One Of Inconsistency",
            "rule" : "sets:ObjectOneOfInconsistencyRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?class rdf:type owl:Class ;
            owl:oneOf ?list .
        ?list rdf:rest*/rdf:first ?member .
        ?resource rdf:type ?class .
        {
            SELECT DISTINCT (COUNT(DISTINCT ?concept ) AS ?conceptCount )
            WHERE 
            {
                ?concept rdf:type owl:Class ;
                    owl:oneOf ?list .
                ?individual rdf:type ?concept .
                ?list rdf:rest*/rdf:first ?member .
                FILTER( ?individual = ?member )
            }
        }
        FILTER( ?conceptCount = 0 )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{class}} has a one of relationship with {{list}}, and {{resource}} is not in {{list}}, the assertion {{resource}} is a {{class}} leads to an inconsistency."# may need to revisit.. do we also check owl:differentFrom?
        },
        Data_One_Of = { # See 7.4 Enumeration of Literals -- still need to come back to this to test if it works
            "reference" : "Data One Of",
            "rule" : "sets:DataOneOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?datatypeProperty rdf:type owl:DatatypeProperty ;
            rdfs:range [ rdf:type owl:DataRange ;
                owl:oneOf ?list ] .
        ?resource ?datatypeProperty ?value .
        ?list rdf:rest*/rdf:first ?member .
        {
            SELECT DISTINCT (COUNT( DISTINCT ?datatypeProperty ) AS ?dataCount ) 
            WHERE 
            {
                ?datatypeProperty rdf:type owl:DatatypeProperty ;
                rdfs:range [ rdf:type owl:DataRange ;
                    owl:oneOf ?list ] .
                ?individual ?datatypeProperty ?value .
                ?list rdf:rest*/rdf:first ?member .
                FILTER( ?value = ?member )
            }
        }
        FILTER( ?dataCount = 0 )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{datatypeProperty}} is restricted to have a value from {{list}}, and {{resource}} {{datatypeProperty}} {{value}}, but {{value}} is not in {{list}}, an inconsistency occurs."
        }, #need to come back to this
        Object_All_Values_From_One = { # cls-avf -- may be in line with 8.2.2 Universal quantification. may need to check closer
            "reference" : "Object All Values From One",
            "rule" : "sets:ObjectAllValuesFromOneRule",
            "resource" : "?v", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?u rdf:type ?x ; 
            ?p ?v .
        ?p rdf:type owl:ObjectProperty .
        ?x (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:allValuesFrom ?y .''',
            "consequent" : "?v rdf:type ?y .",
            "explanation" : "Since {{x}} has a restriction on {{p}} to have all values from {{y}}, {{u}} rdf:type {{x}}, and {{u}} {{p}} {{v}}, we can infer that {{v}} rdf:type {{y}}."
        },
        Object_All_Values_From_Two = {# scm-avf1
            "reference" : "Object All Values From Two",
            "rule" : "sets:ObjectallValuesFromTwoRule",
            "resource" : "?c1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c1 (owl:equivalentClass*|rdfs:subClassOf*)/owl:allValuesFrom ?y1 ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p .
        ?c2 (owl:equivalentClass*|rdfs:subClassOf*)/owl:allValuesFrom ?y2 ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p .
        ?y1 rdfs:subClassOf ?y2 .''',
            "consequent" : "?c1 rdfs:subClassOf ?c2 .",
            "explanation" : ""
        },
        Object_All_Values_From_Three = {# scm-avf2
            "reference" : "Object All Values From Three",
            "rule" : "sets:ObjectallValuesFromThreeRule",
            "resource" : "?c1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c1 (owl:equivalentClass*|rdfs:subClassOf*)/owl:allValuesFrom ?y ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p1 .
        ?c2 (owl:equivalentClass*|rdfs:subClassOf*)/owl:allValuesFrom ?y ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?p2 .
        ?p1 rdfs:subPropertyOf ?p2 .''',
            "consequent" : "?c2 rdfs:subClassOf ?c1 .",  # why is this reversed? this is from the documentation but should understand why
            "explanation" : ""
        },
        Data_All_Values_From = { # might be correct and maybe aligns with 8.4.3 Literal Value Restriction -- should confirm though
            "reference" : "Data All Values From",
            "rule" : "sets:DataAllValuesFromRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?datatypeProperty ?val .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?class (owl:equivalentClass*|rdfs:subClassOf*)/owl:onProperty ?datatypeProperty ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:allValuesFrom ?value .
        FILTER( DATATYPE( ?val ) != ?value )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "{{resource}} {{datatypeProperty}} {{val}}, but {{val}} does not have the same datatype {{value}} restricted for {{datatypeProperty}} in {{class}}. Since {{resource}} rdf:type {{class}}, an inconsistency occurs."
        },
        Object_Max_Cardinality_One = { # cls-maxc1
            "reference" : "Object Max Cardinality One",
            "rule" : "sets:ObjectMaxCardinalityOneRule",
            "resource" : "?u", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x owl:maxCardinality "0"^^xsd:nonNegativeInteger ;
            owl:onProperty ?p .
        ?u rdf:type ?x ;
            ?p ?y .
        ?p rdf:type owl:ObjectProperty .''',
            "consequent" : "?u rdf:type owl:Nothing .",
            "explanation" : "Since {{p}} is assigned a maximum cardinality of 0 for class {{x}}, {{u}} rdf:type {{x}}, and {{u}} {{p}} {{y}}, an inconsistency occurs."
        },
        Object_Max_Cardinality_Two = { # cls-maxc2
            "reference" : "Object Max Cardinality Two",
            "rule" : "sets:ObjectMaxCardinalityTwoRule",
            "resource" : "?y1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x owl:maxCardinality "1"^^xsd:nonNegativeInteger ;
            owl:onProperty ?p .
        ?u rdf:type ?x ;
            ?p ?y1 , ?y2 .
        ?p rdf:type owl:ObjectProperty .''',
            "consequent" : "?y1 owl:sameAs ?y2 .",
            "explanation" : "Since {{p}} is assigned a maximum cardinality of 1 for class {{x}}, {{u}} rdf:type {{x}}, and {{u}} {{p}} {{y1}} as well as {{u}} {{p}} {{y2}}, we can conclude that {{y1}} is the same as {{y2}}."
        },
        Object_Max_Cardinality_Three = { # See 8.3.2 to confirm encoding
            "reference" : "Object Max Cardinality Three",
            "rule" : "sets:ObjectMaxCardinalityThreeRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?objectProperty ?object .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?objectProperty ;
                owl:maxCardinality ?cardinalityValue ].
        FILTER( ?objectCount > ?cardinalityValue )
        {
            SELECT DISTINCT (COUNT(DISTINCT ?object ) AS ?objectCount ) ?individual ?concept
            WHERE 
            {
                ?individual rdf:type ?concept ;
                    ?objectProperty ?object .
                ?objectProperty rdf:type owl:ObjectProperty .
                ?concept rdfs:subClassOf|owl:equivalentClass
                    [ rdf:type owl:Restriction ;
                        owl:onProperty ?objectProperty ;
                        owl:maxCardinality|owl:cardinality ?cardinalityValue ].
            } GROUP BY ?individual ?concept
        }
        BIND( ?resource AS ?individual )
        BIND( ?class AS ?concept )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{objectProperty}} is assigned a maximum cardinality of {{cardinalityValue}} for class {{class}}, {{resource}} rdf:type {{class}}, and {{resource}} has {{objectCount}} distinct assignments of {{objectProperty}} which is greater than {{cardinalityValue}}, we can conclude that there is an inconsistency associated with {{resource}}."
        },# Still need to check distinctness of object
        Object_Min_Cardinality = {#Works, but for lists of size greater than 1, additional (unnecessary) blank nodes are added. LIMIT 1 on the result would address this, but it is outside the where query --- See 8.3.1 to confirm encoding
            "reference" : "Object Min Cardinality",
            "rule" : "sets:ObjectMinCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?objectProperty ?object .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?objectProperty ;
                owl:minCardinality|owl:cardinality ?cardinalityValue ].
        FILTER( ?objectCount < ?cardinalityValue )
        {
            SELECT DISTINCT ( COUNT ( DISTINCT ?object ) AS ?objectCount )
            WHERE 
            {
                ?resource rdf:type ?class ;
                    ?objectProperty ?object .
                ?objectProperty rdf:type owl:ObjectProperty .
                ?class rdfs:subClassOf|owl:equivalentClass
                    [ rdf:type owl:Restriction ;
                        owl:onProperty ?objectProperty ;
                        owl:minCardinality|owl:cardinality ?cardinalityValue ].
            }
        }''',
            "consequent" : "?resource ?objectProperty [ rdf:type owl:Individual ] .",
            "explanation" : "Since {{objectProperty}} is assigned a minimum cardinality of {{cardinalityValue}} for class {{class}}, {{resource}} rdf:type {{class}}, and {{resource}} has {{objectCount}} distinct assignments of {{objectProperty}} which is less than {{cardinalityValue}}, we can conclude the existence of additional assignments of {{objectProperty}} for {{resource}}."
        },# Still need to check distinctness
            Object_Exact_Cardinality = { # See 8.3.3 to confirm encoding
                "reference" : "Object Exact Cardinality",
                "rule" : "sets:ObjectExactCardinalityRule",
                "resource" : "?resource", 
                "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
                "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?objectProperty ?object .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?objectProperty ;
                owl:cardinality ?cardinalityValue ].
        {
            SELECT DISTINCT (COUNT(DISTINCT ?object ) AS ?objectCount )
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
        FILTER( ?objectCount > ?cardinalityValue )
        BIND( ?resource AS ?individual )''',
                "consequent" : "?resource rdf:type owl:Nothing .",
                "explanation" : "Since {{objectProperty}} is assigned an exact cardinality of {{cardinalityValue}} for class {{class}}, {{resource}} rdf:type {{class}}, and {{resource}} has {{objectCount}} distinct assignments of {{objectProperty}} which is greater than {{cardinalityValue}}, we can conclude that there is an inconsistency associated with {{resource}}."
            },# Still need to check distinctness of object
        Data_Max_Cardinality = { # See 8.5.2 to confirm encoding
            "reference" : "Data Max Cardinality",
            "rule" : "sets:DataMaxCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?dataProperty ?data .
        ?dataProperty rdf:type owl:DatatypeProperty .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?dataProperty ;
                owl:maxCardinality ?cardinalityValue ] .
        {
            SELECT DISTINCT (COUNT(DISTINCT ?data ) AS ?dataCount )
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
        FILTER( ?dataCount > ?cardinalityValue )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{dataProperty}} is assigned a maximum cardinality of {{cardinalityValue}} for class {{class}}, {{resource}} rdf:type {{class}}, and {{resource}} has {{dataCount}} distinct assignments of {{dataProperty}} which is greater than {{cardinalityValue}}, we can conclude that there is an inconsistency associated with {{resource}}."
        },
        Data_Min_Cardinality = { # See 8.5.1 to confirm encoding
            "reference" : "Data Min Cardinality",
            "rule" : "sets:DataMinCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?dataProperty ?data .
        ?dataProperty rdf:type owl:DatatypeProperty .
        ?class rdf:type owl:Class ;
            rdfs:subClassOf|owl:equivalentClass
                [ rdf:type owl:Restriction ;
                    owl:onProperty ?dataProperty ;
                    owl:minCardinality ?cardinalityValue ] .
        {
            SELECT DISTINCT (COUNT(DISTINCT ?data ) AS ?dataCount )
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
        FILTER( ?dataCount < ?cardinalityValue )''',
            "consequent" : "?resource ?dataProperty [ rdf:type rdfs:Datatype ] .",
            "explanation" : "Since {{dataProperty}} is assigned a minimum cardinality of {{cardinalityValue}} for class {{class}}, {{resource}} rdf:type {{class}}, and {{resource}} has {{dataCount}} distinct assignments of {{dataProperty}} which is less than {{cardinalityValue}}, we can conclude the existence of additional assignments of {{dataProperty}} for {{resource}}."
        },
        Data_Exact_Cardinality = { # See 8.5.3 to confirm encoding
            "reference" : "Data Exact Cardinality",
            "rule" : "sets:DataExactCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?dataProperty ?data .
        ?dataProperty rdf:type owl:DatatypeProperty .
        ?class rdf:type owl:Class ; 
            rdfs:subClassOf|owl:equivalentClass
                [ rdf:type owl:Restriction ;
                    owl:onProperty ?dataProperty ;
                    owl:cardinality ?cardinalityValue ] .
        {
            SELECT DISTINCT (COUNT(DISTINCT ?data ) AS ?dataCount )
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
        FILTER( ?dataCount > ?cardinalityValue )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{dataProperty}} is assigned an exact cardinality of {{cardinalityValue}} for class {{class}}, {{resource}} rdf:type {{class}}, and {{resource}} has {{dataCount}} distinct assignments of {{dataProperty}} which is greater than {{cardinalityValue}}, we can conclude that there is an inconsistency associated with {{resource}}."
        }, # -- This is currently only accounting for max. Min accounted for in data min rule
        Object_Union_Of_One = { # cls-uni  -- in line with 8.1.2 Union of CLass Expressions
            "reference" : "Object Union Of One",
            "rule" : "sets:ObjectUnionOfOneRule",
            "resource" : "?y", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c rdf:type owl:Class ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:unionOf ?x .
        ?x rdf:rest*/rdf:first ?ci .
        ?y rdf:type ?ci.''',
            "consequent" : "?y rdf:type ?c .",
            "explanation" : "Since {{y}} is of type one of the members of list {{x}}, and {{c}} owl:unionOf {{x}}, we can infer that {{y}} is of type {{c}}."
        },
        Object_Union_Of_Two = { # scm-uni
            "reference" : "Object Union Of Two",
            "rule" : "sets:ObjectUnionOfTwoRule",
            "resource" : "?c", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c rdf:type owl:Class ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:unionOf ?x .
        ?x rdf:rest*/rdf:first ?ci .
        ''',
            "consequent" : "?ci rdfs:subClassOf ?c .",
            "explanation" : "Since {{c}} is the union of the the members in {{x}}, we can infer each of the members in the list is a subclass of {{c}}."
        },
        Disjoint_Union = { # Not included in OWL-RL  aligns with 9.1.4 Disjoint Union of Class Expressions 
            "reference" : "Disjoint Union",
            "rule" : "sets:DisjointUnionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type owl:Class ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:disjointUnionOf ?list .
        ?list rdf:rest*/rdf:first ?member .
        {
            SELECT DISTINCT ?item ?class WHERE 
            {
                ?class rdf:type owl:Class ;
                    (owl:equivalentClass*|rdfs:subClassOf*)/owl:disjointUnionOf ?list .
                ?list rdf:rest*/rdf:first ?item .
            }
        }
        FILTER( ?resource = ?class )
        FILTER( ?member != ?item )''',
            "consequent" : "?member rdfs:subClassOf ?resource ; owl:disjointWith ?item .",
            "explanation" : "Since the class {{resource}} has a subclass or equivalent class relation with a class that comprises the disjoint union of {{list}}, which contains member {{member}}, we can infer that {{member}} is a subclass of {{resource}} and disjoint with the other members of the list."
        },
        Data_Union_Of_One = { # adapted from cls-uni .. also in line with 7.2 Union of Data Ranges
            "reference" : "Data Union Of One",
            "rule" : "sets:DataUnionOfOneRule",
            "resource" : "?y", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c rdf:type rdfs:Datatype ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:unionOf ?x .
        ?x rdf:rest*/rdf:first ?ci .
        ?y rdf:type ?ci.''',
            "consequent" : "?y rdf:type ?c .",
            "explanation" : "Since {{y}} is of type one of the members of list {{x}}, and {{c}} owl:unionOf {{x}}, we can infer that {{y}} is of type {{c}}."
        },
        Data_Union_Of_Two = { # adapted from scm-uni
            "reference" : "Data Union Of Two",
            "rule" : "sets:DataUnionOfTwoRule",
            "resource" : "?c", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c rdf:type rdfs:Datatype ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:unionOf ?x .
        ?x rdf:rest*/rdf:first ?ci .
        ''',
            "consequent" : "?ci rdfs:subClassOf ?c .",
            "explanation" : "Since {{c}} is the union of the the members in {{x}}, we can infer each of the members in the list is a subclass of {{c}}."
        },
        Object_Complement_Of = { # cls-com -- note the example in 8.1.3 takes into account disjoint classes and if an instance is part of c1 that is disjoint with c2 and c3 owl:complementOf c2 , we can infer that the instance is in c3 -- also from 9.1.4 there is a relationship between complements and disjoint unions
            "reference" : "Object Complement Of",
            "rule" : "sets:ObjectComplementOfRule",
            "resource" : "?x", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x rdf:type ?c1 , ?c2 .
        ?c1 rdf:type owl:Class .
        ?c2 rdf:type owl:Class .
        {?c1 owl:complementOf ?c2 .} 
            UNION 
        {?c2 owl:complementOf ?c1 .}''',
            "consequent" : "?x rdf:type owl:Nothing .",
            "explanation" : "Since {{c1}} and {{c2}} are complementary, {{x}} being of type both {{c1}} and {{c2}} leads to an inconsistency."
        },
        Data_Complement_Of = { # not quite the extent of 7.3 Complement of Data Ranges, where we find the set of data ranges (this may be possible if we encode each of the datatypes), but results in the same inconsistency
            "reference" : "Data Complement Of",
            "rule" : "sets:DataComplementOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?datatype rdf:type rdfs:Datatype ;
            owl:datatypeComplementOf ?complement .
        ?resource ?dataProperty ?value .
        ?dataProperty rdf:type owl:DatatypeProperty ;
            rdfs:range ?datatype .
        FILTER( DATATYPE( ?value ) = ?complement )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{datatype}} is the complement of {{complement}}, {{dataProperty}} has range {{datatype}}, and {{resource}} {{dataProperty}} {{value}}, but {{value}} is of type {{complement}}, an inconsistency occurs."
        },
        Object_Property_Complement_Of = { # how is this supposed to differ from object complement of
            "reference" : "Object Property Complement Of",
            "rule" : "sets:ObjectPropertyComplementOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?class rdf:type owl:Class ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:complementOf 
                [ rdf:type owl:Restriction ;
                owl:onProperty ?objectProperty ;
                owl:someValuesFrom ?restrictedClass ] .
        ?resource rdf:type ?class ;
            ?objectProperty [ rdf:type ?objectClass ] .
        ?objectProperty rdf:type owl:ObjectProperty .
        {
            FILTER( ?objectClass = ?restrictedClass )
        }
        UNION
        {
            ?objectClass rdfs:subClassOf*|owl:equivalentClass ?restrictedClass . 
        }''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{class}} is a subclass of or is equivalent to a class with a complement restriction on the use of {{objectProperty}} to have values from {{restrictedClass}}, and {{resource}} is of type {{class}}, but has the link {{objectProperty}} to have values from an instance of {{restrictedClass}}, an inconsistency occurs." # do we also consider lists or complementary properties here?
        },
        Data_Property_Complement_Of = { # how is this supposed to differ from data complement of
            "reference" : "Data Property Complement Of",
            "rule" : "sets:DataPropertyComplementOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?class rdf:type owl:Class ;
            (owl:equivalentClass*|rdfs:subClassOf*)/owl:complementOf 
                [ rdf:type owl:Restriction ;
                owl:onProperty ?dataProperty ;
                owl:someValuesFrom ?datatype ] .
        ?resource rdf:type ?class ;
            ?dataProperty ?value .
        ?dataProperty rdf:type owl:DatatypeProperty .
        FILTER( DATATYPE( ?value )= ?datatype )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{resource}} is a {{class}} which is equivalent to or a subclass of a class that has a complement of restriction on {{dataProperty}} to have some values from {{datatype}}, {{resource}} {{dataProperty}} {{value}}, but {{value}} has a datatype {{datatype}}, an inconsistency occurs."
        },
        Object_Intersection_Of_One = { # cls-int1  -- not done correctly yet -- when done correctly, will be in line with 8.1.1
            "reference" : "Object Intersection Of One",
            "rule" : "sets:ObjectIntersectionOfOneRule",
            "resource" : "?y", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c rdf:type owl:Class ;
            owl:intersectionOf ?x .
        ?x rdf:rest*/rdf:first ?ci .
        ?y rdf:type ?ci .
        {
            SELECT DISTINCT * WHERE
            {
                ?cp rdf:type owl:Class ;
                    owl:intersectionOf ?xp .
                ?xp rdf:rest*/rdf:first ?cip .
                ?yp rdf:type ?cip .
                
            }
        }
        BIND( ?c AS ?cp ) 
        BIND( ?y AS ?yp ) 
        FILTER( ?ci != ?cip )
        ''',# As currently implemented, i think that is the resource is of type any two members in the list, it gets assigned to be of type class
            "consequent" : "?y rdf:type ?c .",
            "explanation" : "Since {{c}} is the intersection of the the members in {{x}}, and {{y}} is of type each of the members in the list, then we can infer {{y}} is a {{c}}."
        },
        Object_Intersection_Of_Two = { # cls-int2  
            "reference" : "Object Intersection Of Two",
            "rule" : "sets:ObjectIntersectionOfTwoRule",
            "resource" : "?y", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c rdf:type owl:Class ;
            owl:intersectionOf ?x .
        ?x rdf:rest*/rdf:first ?ci .
        ?y rdf:type ?c .
        ''',
            "consequent" : "?y rdf:type ?ci .",
            "explanation" : "Since {{c}} is the intersection of the the members in {{x}}, and {{y}} is of type {{c}}, then we can infer {{y}} is of type each of the members in the list."
        },
        Object_Intersection_Of_Three = { # scm-int  
            "reference" : "Object Intersection Of Two",
            "rule" : "sets:ObjectIntersectionOfTwoRule",
            "resource" : "?y", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?c owl:intersectionOf ?x .
        ?x rdf:rest*/rdf:first ?ci .
        ''',
            "consequent" : "?c rdfs:subClassOf ?ci .",
            "explanation" : "Since {{c}} is the intersection of the the members in {{x}}, we can infer {{c}} is the subclass of each of the members in the list."
        },
        Data_Intersection_Of = { # 7.1 - Intersection of Data Ranges
            "reference" : "Data Intersection Of",
            "rule" : "sets:DataIntersectionOf",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?datatype rdf:type rdfs:Datatype ;
            owl:intersectionOf ?list .
        ?list rdf:rest*/rdf:first ?member .
        ?resource rdf:type ?datatype''',
            "consequent" : "?resource rdf:type ?member .",
            "explanation" : "Since {{resource}} is of type {{?datatype}}, and {{datatype}} is the intersection of all of the elements in {{list}}, we can infer that {{resouurce}} is of type each element in {{list}}."
        },
        Object_Max_Qualified_Cardinality_One = { # cls-maxqc1
            "reference" : "Object Max Qualified Cardinality One",
            "rule" : "sets:ObjectMaxQualifiedCardinalityOneRule",
            "resource" : "?u", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x owl:maxQualifiedCardinality "0"^^xsd:nonNegativeInteger ;
            owl:onProperty ?p ;
            owl:onClass ?c .
        ?u rdf:type ?x ;
            ?p ?y .
        ?y rdf:type ?c .
        ?p rdf:type owl:ObjectProperty .''',
            "consequent" : "?u rdf:type owl:Nothing .",
            "explanation" : "Since {{p}} is assigned a maximum cardinality of 0 for {{x}} on class {{c}}, {{u}} rdf:type {{x}}, {{u}} {{p}} {{y}}, and {{y}} rdf:type {{c}}, an inconsistency occurs."
        },
        Object_Max_Qualified_Cardinality_Two = { # cls-maxqc2
            "reference" : "Object Max Qualified Cardinality Two",
            "rule" : "sets:ObjectMaxQualifiedCardinalityTwoRule",
            "resource" : "?u", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x owl:maxQualifiedCardinality "0"^^xsd:nonNegativeInteger ;
            owl:onProperty ?p ;
            owl:onClass owl:Thing .
        ?u rdf:type ?x ;
            ?p ?y .
        ?p rdf:type owl:ObjectProperty .''',
            "consequent" : "?u rdf:type owl:Nothing .",
            "explanation" : "Since {{p}} is assigned a maximum cardinality of 0 for {{x}} on owl:Thing, {{u}} rdf:type {{x}}, and {{u}} {{p}} {{y}}, an inconsistency occurs."
        },
        Object_Max_Qualified_Cardinality_Three = { # cls-maxqc3
            "reference" : "Object Max Qualified Cardinality Three",
            "rule" : "sets:ObjectMaxQualifiedCardinalityThreeRule",
            "resource" : "?y1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x owl:maxQualifiedCardinality "1"^^xsd:nonNegativeInteger ;
            owl:onProperty ?p ;
            owl:onClass ?c .
        ?u rdf:type ?x ;
            ?p ?y1 , ?y2 .
        ?y1 rdf:type ?c .
        ?y2 rdf:type ?c .
        ?p rdf:type owl:ObjectProperty .''',
            "consequent" : "?y1 owl:sameAs ?y2.",
            "explanation" : "Since {{p}} is assigned a maximum qualified cardinality of 1 for {{x}} on class {{c}}, {{u}} rdf:type {{x}}, {{u}} {{p}} {{y1}} as well as {{u}} {{p}} {{y2}}, and {{y1}} and {{y2}} are both of type {{c}}, we can conclude that {{y1}} is the same as {{y2}}."
        },
        Object_Max_Qualified_Cardinality_Four = { # cls-maxqc4
            "reference" : "Object Max Qualified Cardinality Four",
            "rule" : "sets:ObjectMaxQualifiedCardinalityFourRule",
            "resource" : "?y1", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?x owl:maxQualifiedCardinality "1"^^xsd:nonNegativeInteger ;
            owl:onProperty ?p ;
            owl:onClass owl:Thing .
        ?u rdf:type ?x ;
            ?p ?y1 , ?y2 .
        ?p rdf:type owl:ObjectProperty .''',
            "consequent" : "?y1 owl:sameAs ?y2.",
            "explanation" : "Since {{p}} is assigned a maximum qualified cardinality of 1 for {{x}} on class owl:Thing, {{u}} rdf:type {{x}}, and {{u}} {{p}} {{y1}} as well as {{u}} {{p}} {{y2}}, we can conclude that {{y1}} is the same as {{y2}}."
        },
        Object_Max_Qualified_Cardinality_Five = { # original max cardinality rule that accounts for more than just 0 and 1
            "reference" : "Object Max Qualified Cardinality Five",
            "rule" : "sets:ObjectMaxQualifiedCardinalityFiveRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?objectProperty ?object .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?object rdf:type ?restrictedClass .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?objectProperty ;
                owl:onClass ?restrictedClass ;
                owl:maxQualifiedCardinality ?cardinalityValue ].
        FILTER( ?objectCount > ?cardinalityValue )
        {
            SELECT DISTINCT ( COUNT(DISTINCT ?object ) AS ?objectCount ) ?individual ?concept
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
                        owl:maxQualifiedCardinality|owl:qualifiedCardinality ?cardinalityValue ].
            } GROUP BY ?individual ?concept
        }
        BIND( ?resource AS ?individual )
        BIND( ?class AS ?concept )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{class}} is constrained with a qualified max cardinality restriction on property {{objectProperty}} to have a max of {{value}} objects of type class {{restrictedClass}}, and {{resource}} is a {{class}} but has {{objectCount}} objects assigned to {{objectProperty}} which is more than {{value}}, we can infer that an inconsistency occurs."
        },
        Object_Min_Qualified_Cardinality = {
            "reference" : "Object Min Qualified Cardinality",
            "rule" : "sets:ObjectMinQualifiedCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?objectProperty ?object .
        ?object rdf:type ?restrictedClass .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?objectProperty ; 
                owl:minQualifiedCardinality|owl:qualifiedCardinality ?value ;
                owl:onClass ?restrictedClass ] .
        {
            SELECT (COUNT( DISTINCT ?object ) AS ?objectCount ) ?individual ?concept WHERE 
            {          
                ?individual rdf:type ?concept ;
                    ?objectProperty ?object .
                ?object rdf:type ?restrictedClass .
                ?objectProperty rdf:type owl:ObjectProperty .
                ?concept rdfs:subClassOf|owl:equivalentClass
                    [ rdf:type owl:Restriction ;
                        owl:onProperty ?objectProperty ; 
                        owl:minQualifiedCardinality|owl:qualifiedCardinality ?value ;
                        owl:onClass ?restrictedClass ] .
            } GROUP BY ?individual ?concept
        }
        BIND( ?resource AS ?individual )
        BIND( ?class AS ?concept )
        FILTER( ?objectCount < ?value )''',
            "consequent" : "?resource ?objectProperty [ rdf:type owl:Individual ] .",
            "explanation" : "Since {{class}} is constrained with a qualified min cardinality restriction on property {{objectProperty}} to have a min of {{value}} objects of type class {{restrictedClass}}, and {{resource}} is a {{class}} but has {{objectCount}} objects assigned to {{objectProperty}} which is less than {{value}}, we can infer the existence of another object."
        },
        Object_Exact_Qualified_Cardinality = { 
            "reference" : "Object Exact Qualified Cardinality",
            "rule" : "sets:ObjectExactQualifiedCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
            SELECT DISTINCT (COUNT(DISTINCT ?object ) AS ?objectCount ) ?individual ?concept
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
        BIND( ?resource AS ?individual )
        BIND( ?class AS ?concept )
        FILTER( ?objectCount > ?cardinalityValue )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{class}} is constrained with a qualified cardinality restriction on property {{objectProperty}} to have {{value}} objects of type class {{restrictedClass}}, and {{resource}} is a {{class}} but has {{objectCount}} objects assigned to {{objectProperty}}, an inconsistency occurs."
        },
        Data_Max_Qualified_Cardinality = {
            "reference" : "Data Max Qualified Cardinality",
            "rule" : "sets:DataMaxQualifiedCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?datatypeProperty ?value .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?restriction rdf:type owl:Restriction ;
            owl:onProperty ?datatypeProperty ;
            owl:onDataRange ?datatype ;
            owl:maxQualifiedCardinality ?cardinalityValue .
        {
            SELECT DISTINCT (COUNT(DISTINCT ?value ) AS ?valueCount ) ?individual WHERE
            {
                ?individual ?datatypeProperty ?value .
                ?datatypeProperty rdf:type owl:DatatypeProperty .
                ?restriction rdf:type owl:Restriction ;
                    owl:onProperty ?datatypeProperty ;
                    owl:onDataRange ?datatype ;
                    owl:maxQualifiedCardinality ?cardinalityValue .
            } GROUP BY ?individual
        }
        BIND( ?resource AS ?individual )
        FILTER( DATATYPE( ?value ) = ?datatype )
        FILTER( ?valueCount > ?cardinalityValue )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{datatypeProperty}} is constrained with a qualified max cardinality restriction on datatype {{datatype}} to have a max of {{cardinalityValue}} values, and {{resource}} has {{valueCount}} values of type {{datatype}} for property {{datatypeProperty}}, an inconsistency occurs."
        },
        Data_Min_Qualified_Cardinality = {
            "reference" : "Data Min Qualified Cardinality",
            "rule" : "sets:DataMinQualifiedCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?datatypeProperty ?value .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?restriction rdf:type owl:Restriction ;
            owl:onProperty ?datatypeProperty ;
            owl:minQualifiedCardinality ?cardinalityValue ;
            owl:onDataRange ?datatype .
        {
            SELECT (COUNT(DISTINCT ?value ) AS ?valueCount ) ?individual WHERE
            {
                ?individual ?datatypeProperty ?value .
                ?datatypeProperty rdf:type owl:DatatypeProperty .
                ?restriction rdf:type owl:Restriction ;
                    owl:onProperty ?datatypeProperty ;
                    owl:minQualifiedCardinality ?cardinalityValue ;
                    owl:onDataRange ?datatype .
            } GROUP BY ?individual
        }
        BIND( ?resource AS ?individual )
        FILTER( DATATYPE( ?value ) = ?datatype )
        FILTER( ?valueCount < ?cardinalityValue )''',
            "consequent" : "?resource ?datatypeProperty [ rdf:type rdfs:Datatype ] .",
            "explanation" : "Since {{datatypeProperty}} is constrained with a qualified min cardinality restriction on datatype {{datatype}} to have a min of {{cardinalityValue}} values, and {{resource}} has {{valueCount}} values of type {{datatype}} for property {{datatypeProperty}}, we can infer the existence of at least one more additional value."
        },
        Data_Exact_Qualified_Cardinality = {
            "reference" : "Data Exact Qualified Cardinality",
            "rule" : "sets:DataExactQualifiedCardinalityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?datatypeProperty ?value .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?restriction rdf:type owl:Restriction ;
            owl:onProperty ?datatypeProperty ;
            owl:onDataRange ?datatype ;
            owl:qualifiedCardinality ?cardinalityValue .
        {
            SELECT DISTINCT (COUNT(DISTINCT ?value ) AS ?valueCount ) ?individual WHERE
            {
                ?individual ?datatypeProperty ?value .
                ?datatypeProperty rdf:type owl:DatatypeProperty .
                ?restriction rdf:type owl:Restriction ;
                    owl:onProperty ?datatypeProperty ;
                    owl:onDataRange ?datatype ;
                    owl:qualifiedCardinality ?cardinalityValue .
            } GROUP BY ?individual
        }
        BIND( ?resource AS ?individual )
        FILTER( DATATYPE( ?value ) = ?datatype )
        FILTER( ?valueCount > ?cardinalityValue )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{datatypeProperty}} is constrained with a qualified cardinality restriction on datatype {{datatype}} to have {{cardinalityValue}} values, and {{resource}} has {{valueCount}} values of type {{datatype}} for property {{datatypeProperty}}, an inconsistency occurs."# currently the same as qualified max. need to incorporate min requirement
        },
        Datatype_Restriction = { # See 7.5 Datatype restrictions -- this implementation allows min and max, but there is surely more types of restrictions possible
            "reference" : "Datatype Restriction",
            "rule" : "sets:DatatypeRestrictionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
        FILTER( ?value < ?minValue || ?value > ?maxValue )''',# assuming with restriction of the form min exclusive max exclusive
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{class}} has a with restriction on datatype property {{dataProperty}} to be within the range specified in {{list}} with min value {{minValue}} and max value {{maxValue}}, and {{resource}} is of type {{class}} and has a value {{value}} for {{dataProperty}} which is outside the specified range, an inconsistency occurs."
        },
        All_Disjoint_Classes = { # cax-adc
            "reference" : "All Disjoint Classes",
            "rule" : "sets:AllDisjointClassesRule",
            "resource" : "?member", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
        BIND( ?restriction AS ?restrict )
        FILTER( ?member != ?item )''', 
            "consequent" : "?member owl:disjointWith ?item .",
            "explanation" : "Since {{restriction}} is an all disjoint classes restriction with classes listed in {{list}}, each member in {{list}} is disjoint with each other member in the list."
        },
        All_Disjoint_Properties = { # prp-adp
            "reference" : "All Disjoint Properties",
            "rule" : "sets:AllDisjointPropertiesRule",
            "resource" : "?restriction", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
        BIND( ?restriction AS ?restrict ) 
        FILTER( ?member != ?item )''',
            "consequent" : "?member owl:propertyDisjointWith ?item .",
            "explanation" : "Since {{restriction}} is an all disjoint properties restriction with properties listed in {{list}}, each member in {{list}} is disjoint with each other property in the list."
        },
        Object_Property_Chain_Inclusion = { # prp-spo2 -- still need to implement correctly
            "reference" : "Object Property Chain Inclusion",
            "rule" : "sets:ObjectPropertyChainInclusionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?objectProperty rdf:type owl:ObjectProperty ;
            owl:propertyChainAxiom ?list .
        ?list rdf:first ?prop1 .
        ?list rdf:rest/rdf:first ?prop2 .
        ?resource ?prop1 [ ?prop2 ?o ] .''',
            "consequent" : "?resource ?objectProperty ?o .",
            "explanation" : ""#currently limited to two properties
        }
    )
    return InferenceRules


Same_Individual = [ "Triple Reference" , "Same As Symmetry" , "Same As Transitivity" ,  "Same Subject" , "Same Property" , "Same Object"]
Property_Domain = [ "Property Domain One" , "Property Domain Two" , "Property Domain Three" ]
Property_Range = [ "Property Range One" , "Property Range Two" , "Property Range Three" ]
Object_Property_Inclusion = [ "Object Property Inclusion One" , "Object Property Inclusion Two" ] 
Data_Property_Inclusion = [ "Data Property Inclusion One" , "Data Property Inclusion Two" ]
Class_Equivalence = [ "Class Equivalence One" , "Class Equivalence Two" , "Class Equivalence Three" , "Class Equivalence Four" ]
Object_Property_Equivalence = [ "Object Property Equivalence One" , "Object Property Equivalence Two" , "Object Property Equivalence Three" , "Object Property Equivalence Four" ]
Data_Property_Equivalence = [ "Data Property Equivalence One" , "Data Property Equivalence Two" , "Data Property Equivalence Three" , "Data Property Equivalence Four" ]
Object_Property_Inversion = [ "Object Property Inversion One" , "Object Property Inversion Two" ]
Object_Some_Values_From = [ "Object Some Values From One" , "Object Some Values From Two" , "Object Some Values From Three" ]
Object_Has_Value = [ "Object Has Value One" , "Object Has Value Two" ]
Object_One_Of = [ "Object One Of Membership" , "Object One Of Inconsistency" ]
Object_All_Values_From = [ "Object All Values From One" , "Object All Values From Two" , "Object All Values From Three" ]
Object_Max_Cardinality = [ "Object Max Cardinality One" , "Object Max Cardinality Two" , "Object Max Cardinality Three" ]
Object_Max_Qualified_Cardinality = [ "Object Max Qualified Cardinality One" , "Object Max Qualified Cardinality Two" , "Object Max Qualified Cardinality Three" , "Object Max Qualified Cardinality Four" , "Object Max Qualified Cardinality Five" ]
Object_Union_Of = [ "Object Union Of One" , "Object Union Of Two" ]
Object_Intersection_Of = [ "Object Intersection Of One" , "Object Intersection Of Two" , "Object Intersection Of Three" ]
Object_Property_Reflexivity = [ "Object Property Reflexivity One", "Object Property Reflexivity Two" ]
Data_Union_Of = [ "Data Union Of One", "Data Union Of Two"]
Object_Has_Self = [ "Object Has Self One", "Object Has Self Two"]

def get_owl_el_list():
    OWL_EL = [
        "Class Inclusion",
        "Individual Inclusion",
        "Class Disjointness",
        "Object Property Definition",
        "Data Property Definition",
        "Object Property Transitivity",
        "Functional Data Property",
        "Different Individuals",
        "All Different Individuals",
        "Class Assertion",
        "Positive Object Property Assertion",
        "Positive Data Property Assertion",
        "Negative Object Property Assertion",
        "Negative Data Property Assertion",
        "Keys",
        "Data Some Values From",
        "Data Has Value",
        "Data One Of",
        "Data Intersection Of",
        "Object Property Chain Inclusion",
    ] + Same_Individual + Property_Domain + Property_Range + Class_Equivalence + Object_Property_Inclusion + Data_Property_Inclusion + Object_Property_Equivalence + Data_Property_Equivalence + Object_One_Of + Object_Some_Values_From + Object_Intersection_Of + Object_Has_Value + Object_Property_Reflexivity + Object_Has_Self

    return OWL_EL

def get_owl_rl_list():
    OWL_RL = [ # Note that only disjoint union and object property reflexitivity are not supported
        "Class Disjointness",
        "Object Property Transitivity",
        "Functional Data Property",
        "Functional Object Property",
        "Object Property Irreflexivity",
        "Object Property Definition",
        "Data Property Definition",
        "Inverse Functional Object Property",
        "Object Property Disjointness",
        "Data Property Disjointness",
        "Object Property Symmetry",
        "Object Property Asymmetry",
        "Class Inclusion",
        "Individual Inclusion",
        "Different Individuals",
        "All Different Individuals",
        "Class Assertion",
        #"Positive Object Property Assertion",
        #"Positive Data Property Assertion",
        "Negative Object Property Assertion",
        "Negative Data Property Assertion",
        "Keys",
        "Data Some Values From",
        "Data Has Value",
        "Data One Of",
        "Data All Values From",
        "Object Min Cardinality",
        "Object Exact Cardinality",
        "Object Min Qualified Cardinality",
        "Object Exact Qualified Cardinality",
        "Data Max Cardinality",
        "Data Min Cardinality",
        "Data Exact Cardinality",
        "Data Max Qualified Cardinality",
        "Data Min Qualified Cardinality",
        "Data Exact Qualified Cardinality",
        "Datatype Restriction",
        "Object Property Complement Of"
    ] + Same_Individual + Property_Domain + Property_Range + Class_Equivalence + Object_Property_Inclusion + Data_Property_Inclusion + Object_Property_Equivalence + Data_Property_Equivalence + Object_One_Of + Object_Some_Values_From + Object_Intersection_Of + Object_Has_Value + Object_Property_Inversion + Object_All_Values_From + Object_Max_Cardinality + Object_Max_Qualified_Cardinality + Object_Union_Of + Data_Union_Of + Object_Has_Self
    return OWL_RL

def get_owl_ql_list():
    OWL_QL = [
        "Class Inclusion",
        "Individual Inclusion",
        "Class Disjointness",
        "Object Property Definition",
        "Data Property Definition",
        "Object Property Inversion",
        "Object Property Inclusion",
        "Object Property Equivalence",
        "Data Property Equivalence",
        "Object Property Disjointness",
        "Data Property Disjointness",
        "Object Property Symmetry",
        "Object Property Irreflexivity",
        "Object Property Asymmetry",
        "Different Individuals",
        "All Different Individuals",
        "Class Assertion",
        #"Positive Object Property Assertion",
        #"Positive Data Property Assertion"
        "Object Complement Of", 
        "Object Property Complement Of", 
        "Data Property Complement Of", 
        "Object Some Values From",
        "Data Some Values From",
        "Object Intersection Of",
    ] + Property_Domain + Property_Range + Class_Equivalence + Object_Property_Inclusion + Object_Property_Equivalence + Data_Property_Equivalence + Object_Some_Values_From + Object_Intersection_Of + Object_Property_Inversion + Object_Property_Reflexivity
    return OWL_QL

def get_owl_dl_list():
    OWL_DL =[
        "Class Disjointness",
        "Object Property Definition",
        "Data Property Definition",
        "Object Property Transitivity",
        "Functional Data Property",
        "Functional Object Property",
        "Object Property Irreflexivity",
        "Inverse Functional Object Property",
        "Object Property Disjointness",
        "Data Property Disjointness",
        "Object Property Symmetry",
        "Object Property Asymmetry",
        "Class Inclusion",
        "Individual Inclusion",
        "Object Complement Of",
        "All Different Individuals",
        "All Disjoint Classes",
        "All Disjoint Properties",
        "Data Complement Of",
        "Data Property Complement Of",
        "Different Individuals",
        "Class Assertion",
        "Positive Object Property Assertion",
        "Positive Data Property Assertion",
        "Negative Object Property Assertion",
        "Negative Data Property Assertion",
        "Keys",
        "Data Some Values From",
        "Data Has Value",
        "Object Property Complement Of",
        "Data One Of",
        "Data All Values From",
        "Object Min Cardinality",
        "Object Exact Cardinality",
        "Object Min Qualified Cardinality",
        "Object Exact Qualified Cardinality",
        "Data Max Cardinality",
        "Data Min Cardinality",
        "Data Exact Cardinality",
        "Data Max Qualified Cardinality",
        "Data Min Qualified Cardinality",
        "Data Exact Qualified Cardinality",
        "Datatype Restriction",
        "Disjoint Union",
        "Object Property Chain Inclusion",
        "Data Intersection Of"
    ] + Same_Individual + Property_Domain + Property_Range + Class_Equivalence + Object_Property_Inclusion + Data_Property_Inclusion + Object_Property_Equivalence + Data_Property_Equivalence + Object_One_Of + Object_Some_Values_From + Object_Intersection_Of + Object_Has_Value + Object_Property_Inversion + Object_All_Values_From + Object_Max_Cardinality + Object_Max_Qualified_Cardinality + Object_Union_Of + Object_Property_Reflexivity + Object_Has_Self + Data_Union_Of# Also need minInclusive, maxInclusive <-- included in Datatype restriction but is this enough?
    return OWL_DL
