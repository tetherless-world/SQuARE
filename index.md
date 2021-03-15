# A Validation Ontology for Evaluating Semantic Reasoning Engines*
*This work is partially supported by IBM Research through the AI Horizons Network.

### Abstract
We describe an approach for building a deductive inference engine by encoding each OWL Description Logic (DL) axiom as a SPARQL CONSTRUCT query. While earlier work has proposed SPARQL extensions for various purposes, we find that the complete queries used in SPARQL-based reasoning methods are not publicly available. We were also unable to find a similar approach in the literature in which the OWL DL axioms are represented as SPARQL CONSTRUCT queries. We make openly available the queries, software, and the validation ontology that we use for our methodology. Encoded in this validation ontology are RDF examples for each OWL-DL axiom, allowing for the testing of our reasoning engine at a per axiom basis. We describe our approach in terms of implementation, query formulation, and validation. We evaluate the extent to which we are able to encode DL axioms and discuss the implications of the results. We further discuss future research directions that we are pursuing. The approach described in this paper has benefits related to inference engine customization capabilities and of being able to reason over inconsistent knowledge. This work is motivated by potential applications involving hybrid reasoning, distributed reasoning, and explainability in reasoning by embedding provenance in the form of nanopublications.

## Resources

### Ontology

### SPARQL CONSTRUCT Axioms
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

_superClass_ is equivalent to _equivClass_, so since _resource_ is a _superClass_, it is also a _equivClass_



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
