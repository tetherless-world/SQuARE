import twc_square
import os

RulesDict = twc_square.get_rules()
EL_list = twc_square.get_owl_el_list()
RL_list = twc_square.get_owl_rl_list()
QL_list = twc_square.get_owl_ql_list()
DL_list = twc_square.get_owl_dl_list()

triplestore_endpoint = "http://192.168.1.11:9999/blazegraph/sparql"

prefixes = ""
active_list = DL_list 
max_iterations = 10
output = "inferences.nt"
output_file_name = ""
output_extension = ""
mime_type = ""

if "." in output :
    output_string=output.split(".")
    output_file_name = output_string[0]
    output_extension = "." + output_string[1]
    if output_string[1] == "rdf" :
        mime_type = "application/rdf+xml"
    elif output_string[1] == "nt" :
        mime_type = "text/plain"
    elif output_string[1] == "ttl" :
        mime_type = "application/x-turtle"
    elif output_string[1] == "ntx" :
        mime_type = "application/x-n-triples-RDR" 
    elif output_string[1] == "ttlx" :
        mime_type = "application/x-turtle-RDR"
    elif output_string[1] == "n3" :
        mime_type = "text/rdf+n3"
    elif output_string[1] == "trix" :
        mime_type = "application/trix"
    elif output_string[1] == "trig" :
        mime_type = "application/x-trig"
    elif output_string[1] == "nq" :
        mime_type = "text/x-nquads"
    elif output_string[1] == "srj" :
        mime_type = "application/sparql-results+json"
    elif output_string[1] == "json" :
        mime_type = "application/json"
    else :
        mime_type = "text/plain"
else :
    output_file_name = output
    output_extension = ".nt"
    mime_type = "text/plain"

i = 0 
while i < max_iterations :
    for axiom in active_list :
        entry = RulesDict.get(axiom.replace(" ","_"))
        if entry is not None :
            for prefix in entry.get("prefixes") :
                prefixes+= "PREFIX " + prefix + ": <" + entry.get("prefixes")[prefix] + "> "
        
            os.system("curl -X POST " + triplestore_endpoint +" --data-urlencode 'query=" + prefixes + "CONSTRUCT { " + entry.get("consequent") + "} WHERE { "+ entry.get("antecedent") +" FILTER NOT EXISTS { " + entry.get("consequent") + "} }' -H 'Accept:" + mime_type +"' >> " + output_file_name + output_extension)
        else :
            active_list.remove(axiom)
        prefixes = ""
    i += 1
os.system("curl -X POST -H 'Content-Type:" + mime_type + "' --data-binary '@" + output_file_name + output_extension +"' " + triplestore_endpoint)
