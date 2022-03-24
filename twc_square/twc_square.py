def get_rules() :
    InferenceRules = dict(
        Class_Disjointness = {
            "reference" : "Class Disjointness",
            "rule" : "sets:ClassDisjointnessRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class .
        ?resource rdf:type ?disjointClass .
        { ?class owl:disjointWith ?disjointClass . } 
            UNION
        { ?disjointClass owl:disjointWith ?class . }''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{class}} is a disjoint with {{disjointClass}}, any resource that is an instance of {{class}} is not an instance of {{disjointClass}}. Therefore, since {{resource}} is an instance of {{class}}, it can not be an instance of {{disjointClass}}."
        },
        Object_Property_Transitivity = {
            "reference" : "Object Property Transitivity",
            "rule" : "sets:ObjectPropertyTransitivityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?transitiveProperty ?o1 .
        ?o1  ?transitiveProperty ?o2 .
        ?transitiveProperty rdf:type owl:TransitiveProperty .''',
            "consequent" : "?resource ?transitiveProperty ?o2 .",
            "explanation" : "Since {{transitiveProperty}} is a transitive object property, and the relationships {{resource}} {{transitiveProperty}} {{o1}} and {{o1}} {{transitiveProperty}} {{o2}} exist, then we can infer that {{resource}} {{transitiveProperty}} {{o2}}."
        },
        Object_Property_Reflexivity = {
            "reference" : "Object Property Reflexivity",
            "rule" : "sets:ObjectPropertyReflexivityRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?type ;
            ?reflexiveProperty ?o .
        ?o rdf:type ?type .
        ?reflexiveProperty rdf:type owl:ReflexiveProperty .''',
            "consequent" : "?resource ?reflexiveProperty ?resource .",
            "explanation" : "Since {{resource}} has a {{reflexiveProperty}} assertion to {{o}}, {{resource}} and {{o}} are both of type {{type}}, and {{reflexiveProperty}} is a reflexive property, we can infer that {{resource}} {{reflexiveProperty}} {{resource}}."
        },
        Property_Domain = {
            "reference" : "Property Domain",
            "rule" : "sets:PropertyDomainRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdfs:domain ?class .''',
            "consequent" : "?resource rdf:type ?class .",
            "explanation" : "Since the domain of {{p}} is {{class}}, this implies that {{resource}} is a {{class}}."
        },
        Property_Range = {
            "reference" : "Property Range",
            "rule" : "sets:PropertyRangeRule",
            "resource" : "?resource",
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdfs:range ?class .''',
            "consequent" : "?o rdf:type ?class .",
            "explanation" : "Since the range of {{p}} is {{class}}, this implies that {{o}} is a {{class}}."
        },
        Functional_Data_Property = {
            "reference" : "Functional Data Property",
            "rule" : "sets:FunctionalDataPropertyRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?functionalProperty ?o1 ,
                ?o2 .
        ?functionalProperty rdf:type owl:DatatypeProperty ,
                owl:FunctionalProperty .
        FILTER (str(?o1) !=  str(?o2))''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{functionalProperty}} is a functional data property, {{resource}} can only have one value for {{functionalProperty}}. Since {{resource}} {{functionalProperty}} both {{o1}} and {{o2}}, and {{o1}} is different from {{o2}}, an inconsistency occurs."
        },
        Functional_Object_Property = {
            "reference" : "Functional Object Property",
            "rule" : "sets:FunctionalObjectPropertyRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?functionalProperty ?o1 ,
                ?o2 .
        ?functionalProperty rdf:type owl:ObjectProperty , 
                owl:FunctionalProperty .
        FILTER (str( ?o1 ) !=  str( ?o2 ))''',
            "consequent" : "?o1 owl:sameAs ?o2 .",
            "explanation" : "Since {{functionalProperty}} is a functional object property, {{resource}} can only have one value for {{functionalProperty}}. Since {{resource}} {{functionalProperty}} both {{o1}} and {{o2}}, we can infer that {{o1}} and {{o2}} must be the same individual."
        },
        Property_Disjointness = {
            "reference" : "Property Disjointness",
            "rule" : "sets:PropertyDisjointnessRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?p1 ?o1 ,
                ?o2 .
        ?resource ?p2 ?o2 .
        {?p1 owl:propertyDisjointWith ?p2 .}
            UNION
        {?p2 owl:propertyDisjointWith ?p1 .}''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since properties {p1} and {p2} are disjoint, {{resource}} having both {{p2}} {{o2}} as well as {{p1}} {{o2}} leads to an inconsistency. "
        },
        Object_Property_Asymmetry = {
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
        Object_Property_Symmetry = {
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
        Object_Property_Irreflexivity = {
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
        Class_Inclusion = {
            "reference" : "Class Inclusion",
            "rule" : "sets:ClassInclusionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdfs:subClassOf ?class .
        ?class rdfs:subClassOf+ ?superClass .''',
            "consequent" : "?resource rdfs:subClassOf ?superClass .",
            "explanation" : "Since {{class}} is a subclass of {{superClass}}, any class that is a subclass of {{class}} is also a subclass of {{superClass}}. Therefore, {{resource}} is a subclass of {{superClass}}."
        },
        Individual_Inclusion = {
            "reference" : "Individual Inclusion",
            "rule" : "sets:IndividualInclusionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class .
        ?class rdfs:subClassOf+ ?superClass .''',
            "consequent" : "?resource rdf:type ?superClass .",
            "explanation" : "Any instance of {{class}} is also an instance of {{superClass}}. Therefore, since {{resource}} is a {{class}}, it also is a {{superClass}}."
        },
        Property_Inclusion = {
            "reference" : "Property Inclusion",
            "rule" : "sets:PropertyInclusionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdf:type owl:Property ;
            rdfs:subPropertyOf+ ?superProperty .''',
            "consequent" : "?resource ?superProperty ?o .",
            "explanation" : "Any subject and object related by the property {{p}} is also related by {{superProperty}}. Therefore, since {{resource}} {{p}} {{o}}, it is implied that {{resource}} {{superProperty}} {{o}}."
        },
        Object_Property_Inclusion = {
            "reference" : "Object Property Inclusion",
            "rule" : "sets:ObjectPropertyInclusionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdf:type owl:ObjectProperty ;
            rdfs:subPropertyOf+ ?superProperty .''',
            "consequent" : "?resource ?superProperty ?o .",
            "explanation" : "Any subject and object related by the property {{p}} is also related by {{superProperty}}. Therefore, since {{resource}} {{p}} {{o}}, it is implied that {{resource}} {{superProperty}} {{o}}."
        },
        Data_Property_Inclusion = {
            "reference" : "Data Property Inclusion",
            "rule" : "sets:DataPropertyInclusionRule",
            "resource" : "?resource",
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdf:type owl:DatatypeProperty ;
            rdfs:subPropertyOf+ ?superProperty .''',
            "consequent" : "?resource ?superProperty ?o .",
            "explanation" : "Any subject and object related by the property {{p}} is also related by {{superProperty}}. Therefore, since {{resource}} {{p}} {{o}}, it is implied that {{resource}} {{superProperty}} {{o}}."
        },
        Class_Equivalence = {
            "reference" : "Class Equivalence",
            "rule" : "sets:ClassEquivalenceRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource rdf:type ?superClass .
        {?superClass owl:equivalentClass ?equivClass .}
            UNION
        {?equivClass owl:equivalentClass ?superClass .}''', 
            "consequent" : "?resource rdf:type ?equivClass .",
            "explanation" : "{{superClass}} is equivalent to {{equivClass}}, so since {{resource}} is a {{superClass}}, it is also a {{equivClass}}."
        },
        Property_Equivalence = {
            "reference" : "Property Equivalence",
            "rule" : "sets:PropertyEquivalenceRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        {?p owl:equivalentProperty ?equivProperty .}
            UNION
        {?equivProperty owl:equivalentProperty ?p . }''', 
            "consequent" : "?resource ?equivProperty ?o .",
            "explanation" : "The properties {{p}} and {{equivProperty}} are equivalent. Therefore, since {{resource}} {{p}} {{o}}, it is implied that {{resource}} {{equivProperty}} {{o}}."
        },
        Object_Property_Inversion = {
            "reference" : "Object Property Inversion",
            "rule" : "sets:ObjectPropertyInversionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdf:type owl:ObjectProperty .
        {?p owl:inverseOf ?inverseProperty .}
            UNION
        {?inverseProperty owl:inverseOf ?p .}''', 
            "consequent" : "?o ?inverseProperty ?resource .",
            "explanation" : "The object properties {{p}} and {{inverseProperty}} are inversely related to eachother. Therefore, since {{resource}} {{p}} {{o}}, it is implied that {{o}} {{inverseProperty}} {{resource}}."
        },
        Same_Individual = {
            "reference" : "Same Individual",
            "rule" : "sets:SameIndividualRule",
            "resource" : "?individual", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        {
            ?resource owl:sameAs ?individual .
        }
            UNION
        {
            ?individual owl:sameAs ?resource .
        }
        ?resource ?p ?o .''', 
            "consequent" : "?individual ?p ?o .",
            "explanation" : "Since {{resource}} is the same as {{individual}}, they share the same properties."#except maybe for annotation properties? should possibly add this check in
        },
        Different_Individuals = {
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
        All_Different_Individuals = {
            "reference" : "All Different Individuals",
            "rule" : "sets:AllDifferentIndividualsRule",
            "resource" : "?restriction", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
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
        BIND( ?restriction AS ?restrict ) 
        FILTER( ?member != ?item )''', 
            "consequent" : "?member owl:differentFrom ?item .",
            "explanation" : "Since {{restriction}} is an all different restriction with individuals listed in {{list}}, each member in {{list}} is different from each other member in the list."
        },
        Class_Assertion = {
            "reference" : "Class Assertion",
            "rule" : "sets:ClassAssertionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource rdf:type ?class .
        ?class rdf:type owl:Class ;
            rdfs:subClassOf+ ?superClass .''', 
            "consequent" : "?resource rdf:type ?superClass .",
            "explanation" : "Since {{class}} is a subclass of {{superClass}}, any individual that is an instance of {{class}} is also an instance of {{superClass}}. Therefore, {{resource}} is an instance of {{superClass}}."
        },
    #        Positive_Object_Property_Assertion = {
    #            "reference" : "Positive Object Property Assertion",
    #            "rule" : "sets:PositiveObjectPropertyAssertionRule",
    #            "resource" : "?resource", 
    #            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
    #            "antecedent" :  '''
    #    ?resource ?objectProperty ?o .
    #    ?objectProperty rdf:type owl:ObjectProperty .
    #    ?class rdf:type owl:Class;
    #        rdfs:subClassOf|owl:equivalentClass
    #            [ rdf:type owl:Restriction ;
    #                owl:onProperty ?objectProperty ;
    #                owl:someValuesFrom owl:Thing ] .''',#may need to come back to this 
    #            "consequent" : "?resource rdf:type ?class .",
    #            "explanation" : "Since {{resource}} {{objectProperty}} {{o}}, and {{class}} has an object property restriction on {{objectProperty}} to have any value that is an owl:Thing, we can infer that {{resource}} is a {{class}}."
    #        },
    #        Positive_Data_Property_Assertion = { # Need to revisit to include data ranges
    #            "reference" : "Positive Data Property Assertion",
    #            "rule" : "sets:PositiveDataPropertyAssertionRule",
    #            "resource" : "?resource", 
    #            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
    #            "antecedent" :  '''
    #    ?resource ?dataProperty ?o .
    #    ?dataProperty rdf:type owl:DatatypeProperty .
    #    ?class rdf:type owl:Class;
    #        rdfs:subClassOf|owl:equivalentClass
    #            [ rdf:type owl:Restriction ;
    #                owl:onProperty ?dataProperty ;
    #                owl:someValuesFrom ?value ] .
    #    FILTER( DATATYPE( ?o ) = ?value )''', 
    #            "consequent" : "?resource rdf:type ?class .",
    #            "explanation" : "Since {{resource}} {{dataProperty}} {{o}}, and {{class}} has an object property restriction on {{dataProperty}} to have a value of type {{value}}, and {{o}} is of type {{value}}, we can infer that {{resource}} is a {{class}}."
    #        }, # the previous two might just be s p o assertion
        Negative_Object_Property_Assertion = {
            "reference" : "Negative Object Property Assertion",
            "rule" : "sets:NegativeObjectPropertyAssertionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdf:type owl:ObjectProperty .
        ?x rdf:type owl:NegativePropertyAssertion ;
            owl:sourceIndividual ?resource ;
            owl:assertionProperty ?p ;
            owl:targetIndividual ?o .''', 
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since a negative object property assertion was made with source {{resource}}, object property {{p}}, and target individual {{o}}, the existence of {{resource}} {{p}} {{o}} results in an inconsistency."
        },
        Negative_Data_Property_Assertion = {
            "reference" : "Negative Data Property Assertion",
            "rule" : "sets:NegativeDataPropertyAssertionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"},
            "antecedent" :  '''
        ?resource ?p ?o .
        ?p rdf:type owl:DatatypeProperty .
        ?x rdf:type owl:NegativePropertyAssertion ;
            owl:sourceIndividual ?resource ;
            owl:assertionProperty ?p ;
            owl:targetValue ?o .''', 
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since a negative datatype property assertion was made with source {{resource}}, datatype property {{p}}, and target value {{o}}, the existence of {{resource}} {{p}} {{o}} results in an inconsistency."
        },
        Keys = {
            "reference" : "Keys",
            "rule" : "sets:KeysRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?keyProperty ?keyValue .
        ?class rdf:type owl:Class ;
            owl:hasKey ( ?keyProperty ) .
        ?individual rdf:type ?class ;
            ?keyProperty ?keyValue .''',
            "consequent" : "?resource owl:sameAs ?individual .",
            "explanation" : "Since {{class}} has key {{keyProperty}}, {{resource}} and {{individual}} are both of type {{class}}, and {{resource}} and {{individual}} both {{keyProperty}} {{keyValue}}, then {{resource}} and {{individual}} must be the same."
        },
        Inverse_Functional_Object_Property = {
            "reference" : "Inverse Functional Object Property",
            "rule" : "sets:InverseFunctionalObjectPropertyRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?invFunctionalProperty ?o .
        ?individual ?invFunctionalProperty ?o .
        ?invFunctionalProperty rdf:type owl:ObjectProperty ,
                owl:InverseFunctionalProperty .''',
            "consequent" : "?resource owl:sameAs ?individual",
            "explanation" : "Since {{invFunctionalProperty}} is an inverse functional property, and {{resource}} and {{individual}} both have the relationship {{invFunctionalProperty}} {{o}}, then we can infer that {{resource}} is the same as {{individual}}."
        },
        Object_Some_Values_From = {# Should revisit this after confirming test case
            "reference" : "Object Some Values From",
            "rule" : "sets:ObjectSomeValuesFromRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?objectProperty
            [ rdf:type ?valueclass ] .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction;
                owl:onProperty ?objectProperty ;
                owl:someValuesFrom ?valueclass ] .''',
            "consequent" : "?resource rdf:type ?class .",
            "explanation" : "Since {{resource}} {{objectProperty}} an instance of {{valueclass}}, and {{class}} has a restriction on {{objectProperty}} to have some values from {{valueclass}}, we can infer that {{resource}} rdf:type {{class}}."
        },
        Data_Some_Values_From = {
            "reference" : "Data Some Values From",
            "rule" : "sets:DataSomeValuesFromRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?datatypeProperty ?val .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?class rdf:type owl:Class ;
            rdfs:subClassOf|owl:equivalentClass
                [ rdf:type owl:Restriction ;
                    owl:onProperty ?datatypeProperty ;
                    owl:someValuesFrom ?value ] .
        FILTER( DATATYPE( ?val ) != ?value )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "{{resource}} {{datatypeProperty}} {{val}}, but {{val}} does not the same datatype {{value}} restricted for {{datatypeProperty}} in {{class}}. Since {{resource}} rdf:type {{class}}, an inconsistency occurs."
        },#Data some and all values from behave the same as each other..? May need to revisit
        Object_Has_Self = {
            "reference" : "Object Has Self",
            "rule" : "sets:ObjectHasSelfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?objectProperty ;
                owl:hasSelf \"true\"^^xsd:boolean ] .''',
            "consequent" : "?resource ?objectProperty ?resource .",
            "explanation" : "{{resource}} is of type {{class}}, which has a self restriction on the property {{objectProperty}}, allowing us to infer {{resource}} {{objectProperty}} {{resource}}."
        },
        Object_Has_Value = {
            "reference" : "Object Has Value",
            "rule" : "sets:ObjectHasValueRule",
            "resource" : "?resource",
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class .
        ?objectProperty rdf:type owl:ObjectProperty.
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?objectProperty ;
                owl:hasValue ?object ] .''',
            "consequent" : "?resource ?objectProperty ?object .",
            "explanation" : "Since {{resource}} is of type {{class}}, which has a value restriction on {{objectProperty}} to have {{object}}, we can infer that {{resource}} {{objectProperty}} {{object}}."
        },
        Data_Has_Value = {
            "reference" : "Data Has Value",
            "rule" : "sets:DataHasValueRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource ?datatypeProperty ?value .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?class owl:equivalentClass
            [ rdf:type owl:Restriction ;
                owl:onProperty ?datatypeProperty ;
                owl:hasValue ?value ].''',
            "consequent" : "?resource rdf:type ?class .",
            "explanation" : "Since {{class}} is equivalent to the restriction on {{datatypeProperty}} to have value {{value}} and {{resource}} {{datatypeProperty}} {{value}}, we can infer that {{resource}} rdf:type {{class}}."
        },#Note that only owl:equivalentClass results in inference, not rdfs:subClassOf
        Object_One_Of_Membership = {
            "reference" : "Object One Of Membership",
            "rule" : "sets:ObjectOneOfMembershipRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type owl:Class ;
            owl:oneOf ?list .
        ?list rdf:rest*/rdf:first ?member .''',
            "consequent" : "?member rdf:type ?resource .",
            "explanation" : "Since {{resource}} has a one of relationship with {{list}}, the member {{member}} in {{list}} is of type {{resource}}."
        },
        Object_One_Of_Inconsistency = {
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
        Data_One_Of = {
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
        Object_All_Values_From = {
            "reference" : "Object All Values From",
            "rule" : "sets:ObjectAllValuesFromRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?individual rdf:type ?class ; 
            ?objectProperty ?resource .
        ?objectProperty rdf:type owl:ObjectProperty .
        ?class rdfs:subClassOf|owl:equivalentClass
            [ rdf:type owl:Restriction;
                owl:onProperty ?objectProperty ;
                owl:allValuesFrom ?valueclass ] .''',
            "consequent" : "?resource rdf:type ?valueclass .",
            "explanation" : "Since {{class}} has a restriction on {{objectProperty}} to have all values from {{valueclass}}, {{individual}} rdf:type {{class}}, and {{individual}} {{objectProperty}} {{resource}}, we can infer that {{resource}} rdf:type {{valueclass}}."
        },
        Data_All_Values_From = {
            "reference" : "Data All Values From",
            "rule" : "sets:DataAllValuesFromRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ;
            ?datatypeProperty ?val .
        ?datatypeProperty rdf:type owl:DatatypeProperty .
        ?class rdf:type owl:Class ;
            rdfs:subClassOf|owl:equivalentClass
                [ rdf:type owl:Restriction ;
                    owl:onProperty ?datatypeProperty ;
                    owl:allValuesFrom ?value ] .
        FILTER( DATATYPE( ?val ) != ?value )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "{{resource}} {{datatypeProperty}} {{val}}, but {{val}} does not have the same datatype {{value}} restricted for {{datatypeProperty}} in {{class}}. Since {{resource}} rdf:type {{class}}, an inconsistency occurs."
        },
        Object_Max_Cardinality = {
            "reference" : "Object Max Cardinality",
            "rule" : "sets:ObjectMaxCardinalityRule",
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
        Object_Min_Cardinality = {#Works, but for lists of size greater than 1, additional (unnecessary) blank nodes are added. LIMIT 1 on the result would address this, but it is outside the where query
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
            Object_Exact_Cardinality = {
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
        Data_Max_Cardinality = {
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
        Data_Min_Cardinality = {
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
        Data_Exact_Cardinality = {
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
        Object_Union_Of = {
            "reference" : "Object Union Of",
            "rule" : "sets:ObjectUnionOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type owl:Class ;
            rdfs:subClassOf|owl:equivalentClass
                [ rdf:type owl:Class ;
                    owl:unionOf ?list ] .
        ?list rdf:rest*/rdf:first ?member .''',
            "consequent" : "?member rdfs:subClassOf ?resource .",
            "explanation" : "Since the class {{resource}} has a subclass or equivalent class relation with a class that comprises the union of {{list}}, which contains member {{member}}, we can infer that {{member}} is a subclass of {{resource}}."
        },
        Disjoint_Union = {
            "reference" : "Disjoint Union",
            "rule" : "sets:DisjointUnionRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
        FILTER( ?resource = ?class )
        FILTER( ?member != ?item )''',
            "consequent" : "?member rdfs:subClassOf ?resource ; owl:disjointWith ?item .",
            "explanation" : "Since the class {{resource}} has a subclass or equivalent class relation with a class that comprises the disjoint union of {{list}}, which contains member {{member}}, we can infer that {{member}} is a subclass of {{resource}} and disjoint with the other members of the list."
        },
        Data_Union_Of = {
            "reference" : "Data Union Of",
            "rule" : "sets:DataUnionOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
        FILTER( DATATYPE( ?data ) = ?datatype )''', #need to come back and make sure logic is correct on this one
            "consequent" : "?resource rdf:type ?class .",
            "explanation" : ""#add explanation here
        },
        Object_Complement_Of = {
            "reference" : "Object Complement Of",
            "rule" : "sets:ObjectComplementOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
        ?resource rdf:type ?class ,
                ?complementClass .
        ?class rdf:type owl:Class .
        ?complementClass rdf:type owl:Class .
        {?class owl:complementOf ?complementClass .} 
            UNION 
        {?complementClass owl:complementOf ?class .}''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{class}} and {{complementClass}} are complementary, {{resource}} being of type both {{class}} and {{complementClass}} leads to an inconsistency."
        },
        Data_Complement_Of = {
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
        Object_Property_Complement_Of = {
            "reference" : "Object Property Complement Of",
            "rule" : "sets:ObjectPropertyComplementOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
            FILTER( ?objectClass = ?restrictedClass )
        }
        UNION
        {
            ?objectClass rdfs:subClassOf*|owl:equivalentClass ?restrictedClass . 
        }''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{class}} is a subclass of or is equivalent to a class with a complement restriction on the use of {{objectProperty}} to have values from {{restrictedClass}}, and {{resource}} is of type {{class}}, but has the link {{objectProperty}} to have values from an instance of {{restrictedClass}}, an inconsistency occurs." # do we also consider lists or complementary properties here?
        },
        Data_Property_Complement_Of = {
            "reference" : "Data Property Complement Of",
            "rule" : "sets:DataPropertyComplementOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
        FILTER( DATATYPE( ?value )= ?datatype )''',
            "consequent" : "?resource rdf:type owl:Nothing .",
            "explanation" : "Since {{resource}} is a {{class}} which is equivalent to or a subclass of a class that has a complement of restriction on {{dataProperty}} to have some values from {{datatype}}, {{resource}} {{dataProperty}} {{value}}, but {{value}} has a datatype {{datatype}}, an inconsistency occurs."
        },
        Object_Intersection_Of = {
            "reference" : "Object Intersection Of",
            "rule" : "sets:ObjectIntersectionOfRule",
            "resource" : "?resource", 
            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
            "antecedent" :  '''
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
        BIND( ?class AS ?concept ) 
        BIND( ?resource AS ?individual ) 
        FILTER( ?member != ?item )
        ''',# As currently implemented, i think that is the resource is of type any two members in the list, it gets assigned to be of type class
            "consequent" : "?resource rdf:type ?class .",
            "explanation" : "Since {{class}} is the intersection of the the members in {{list}}, and {{resource}} is of type each of the members in the list, then we can infer {{resource}} is a {{class}}."
        },
    #        Data_Intersection_Of = {
    #            "reference" : "Data Intersection Of",
    #            "rule" : "sets:DataIntersectionOf",
    #            "resource" : "?resource", 
    #            "prefixes" : {"owl": "http://www.w3.org/2002/07/owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdfs":"http://www.w3.org/2000/01/rdf-schema#","sets":"http://purl.org/ontology/sets/ont#"}, 
    #            "antecedent" :  '''
    #    ?datatype rdf:type rdfs:Datatype ;
    #        owl:intersectionOf ?list .
    #    ?list rdf:rest*/rdf:first ?member .''',
    #            "consequent" : "?resource rdf:type owl:Nothing .",
    #            "explanation" : ""
    #        },
        Object_Qualified_Max_Cardinality = {
            "reference" : "Object Qualified Max Cardinality",
            "rule" : "sets:ObjectQualifiedMaxCardinalityRule",
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
        Object_Qualified_Min_Cardinality = {
            "reference" : "Object Qualified Min Cardinality",
            "rule" : "sets:ObjectQualifiedMinCardinalityRule",
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
        Object_Qualified_Exact_Cardinality = { 
            "reference" : "Object Qualified Exact Cardinality",
            "rule" : "sets:ObjectQualifiedExactCardinalityRule",
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
        Data_Qualified_Max_Cardinality = {
            "reference" : "Data Qualified Max Cardinality",
            "rule" : "sets:DataQualifiedMaxCardinalityRule",
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
        Data_Qualified_Min_Cardinality = {
            "reference" : "Data Qualified Min Cardinality",
            "rule" : "sets:DataQualifiedMinCardinalityRule",
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
        Data_Qualified_Exact_Cardinality = {
            "reference" : "Data Qualified Exact Cardinality",
            "rule" : "sets:DataQualifiedExactCardinalityRule",
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
        Datatype_Restriction = {
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
        All_Disjoint_Classes = {
            "reference" : "All Disjoint Classes",
            "rule" : "sets:AllDisjointClassesRule",
            "resource" : "?restriction", 
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
        All_Disjoint_Properties = {
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
        Object_Property_Chain_Inclusion = {
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

def get_owl_el_list():
    OWL_EL = [
        "Class Inclusion",
        "Class Equivalence",
        "Class Disjointness",
        "Property Inclusion",
        "Object Property Inclusion",
        "Data Property Inclusion",
        "Property Equivalence",
        "Object Property Transitivity",
        "Object Property Reflexivity",
        "Property Domain",
        "Property Range",
        "Functional Data Property",
        "Same Individual",
        "Different Individuals",
        "Class Assertion",
        #"Positive Object Property Assertion",
        #"Positive Data Property Assertion",
        "Negative Object Property Assertion",
        "Negative Data Property Assertion",
        "Keys",
        "Object Some Values From",
        "Data Some Values From",
        "Object Has Value",
        "Data Has Value",
        "Object Has Self",
        "Object One Of Membership",
        "Object One Of Inconsistency",
        "Data One Of",
        "Object Intersection Of",
        "Data Intersection Of",
    ]
    return OWL_EL

def get_owl_rl_list():
    OWL_RL = [ # Note that only disjoint union and object property reflexitivity are not supported
        "Class Disjointness",
        "Object Property Transitivity",
        "Property Domain",
        "Property Range",
        "Functional Data Property",
        "Functional Object Property",
        "Object Property Irreflexivity",
        "Inverse Functional Object Property",
        "Property Disjointness",
        "Object Property Symmetry",
        "Object Property Asymmetry",
        "Class Inclusion",
        "Property Inclusion",
        "Object Property Inclusion",
        "Data Property Inclusion",
        "Class Equivalence",
        "Property Equivalence",
        "Object Property Inversion",
        "Same Individual",
        "Different Individuals",
        "Class Assertion",
        #"Positive Object Property Assertion",
        #"Positive Data Property Assertion",
        "Negative Object Property Assertion",
        "Negative Data Property Assertion",
        "Keys",
        "Object Some Values From",
        "Data Some Values From",
        "Object Has Self",
        "Object Has Value",
        "Data Has Value",
        "Object One Of Membership",
        "Object One Of Inconsistency",
        "Data One Of",
        "Object All Values From",
        "Data All Values From",
        "Object Max Cardinality",
        "Object Min Cardinality",
        "Object Exact Cardinality",
        "Object Qualified Max Cardinality",
        "Object Qualified Min Cardinality",
        "Object Qualified Exact Cardinality",
        "Data Max Cardinality",
        "Data Min Cardinality",
        "Data Exact Cardinality",
        "Data Qualified Max Cardinality",
        "Data Qualified Min Cardinality",
        "Data Qualified Exact Cardinality",
        "Datatype Restriction",
        "Object Union Of",
        "Data Union Of"
    ]
    return OWL_RL

def get_owl_ql_list():
    OWL_QL = [
        "Class Inclusion",
        "Class Equivalence",
        "Class Disjointness",
        "Object Property Inversion",
        "Property Inclusion",
        "Property Domain",
        "Property Range",
        "Property Disjointness",
        "Object Property Symmetry",
        "Object Property Reflexivity",
        "Object Property Irreflexivity",
        "Object Property Asymmetry",
        "Different Individuals",
        "Class Assertion",
        #"Positive Object Property Assertion",
        #"Positive Data Property Assertion"
        "Object Complement Of",
        "Object Property Complement Of",
        "Data Property Complement Of",
    ]
    return OWL_QL

def get_owl_dl_list():
    OWL_DL =[
        "Class Disjointness",
        "Object Property Transitivity",
        "Property Domain",
        "Property Range",
        "Functional Data Property",
        "Functional Object Property",
        "Object Property Irreflexivity",
        "Inverse Functional Object Property",
        "Property Disjointness",
        "Object Property Symmetry",
        "Object Property Asymmetry",
        "Object Property Reflexivity",
        "Class Inclusion",
        "Property Inclusion",
        "Individual Inclusion",
        "Object Property Inclusion",
        "Data Property Inclusion",
        "Class Equivalence",
        "Property Equivalence",
        "Object Property Inversion",
        "Object Complement Of",
        "Same Individual",
        "All Different Individuals",
        "All Disjoint Classes",
        "All Disjoint Properties",
        "Data Complement Of",
        "Data Property Complement Of",
        "Different Individuals",
        "Class Assertion",
        #"Positive Object Property Assertion",
        #"Positive Data Property Assertion",
        "Negative Object Property Assertion",
        "Negative Data Property Assertion",
        "Keys",
        "Object Some Values From",
        "Data Some Values From",
        "Object Has Self",
        "Object Has Value",
        "Data Has Value",
        "Object Property Complement Of",
        "Object One Of Membership",
        "Object One Of Inconsistency",
        "Data One Of",
        "Object All Values From",
        "Data All Values From",
        "Object Max Cardinality",
        "Object Min Cardinality",
        "Object Exact Cardinality",
        "Object Qualified Max Cardinality",
        "Object Qualified Min Cardinality",
        "Object Qualified Exact Cardinality",
        "Data Max Cardinality",
        "Data Min Cardinality",
        "Data Exact Cardinality",
        "Data Qualified Max Cardinality",
        "Data Qualified Min Cardinality",
        "Data Qualified Exact Cardinality",
        "Datatype Restriction",
        "Data Union Of",
        "Disjoint Union",
        "Object Union Of",
        "Object Property Chain Inclusion",
        "Object Intersection Of",
        "Data Intersection Of"
    ] # Also need minInclusive, maxInclusive <-- included in Datatype restriction but is this enough?
    return OWL_DL
