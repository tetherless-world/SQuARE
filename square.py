import twc_square
import os
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

RulesDict = twc_square.get_rules()
EL = twc_square.get_owl_el_list()
RL = twc_square.get_owl_rl_list()
QL = twc_square.get_owl_ql_list()
DL = twc_square.get_owl_dl_list()
print(DL)
triplestore_endpoint = config['DEFAULT']['triplestore_endpoint']

prefixes = ""

profile = config['DEFAULT']['profile']
if profile == "DL" :
    active_list = DL
elif profile == "RL" :
    active_list = RL
elif profile == "QL" :
    active_list = QL
elif profile == "EL" :
    active_list = EL
else :
    active_list = RL
    
max_iterations =  int(config['DEFAULT']['max_iterations'])
output = config['DEFAULT']['output_file'] #"inferences.nt"

output_file_name = ""
output_extension = ""
mime_type = ""
temp_file_name = "temp"
save_output = config.getboolean('DEFAULT','save_output')

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
            if save_output == True :
                os.system("curl -X POST " + triplestore_endpoint +" --data-urlencode 'query=" + prefixes + "CONSTRUCT { " + entry.get("consequent") + "} WHERE { "+ entry.get("antecedent") +" FILTER NOT EXISTS { " + entry.get("consequent") + "} }' -H 'Accept:" + mime_type +"' | tee " + temp_file_name + output_extension + " >> " + output_file_name + output_extension)
            else :
                os.system("curl -X POST " + triplestore_endpoint +" --data-urlencode 'query=" + prefixes + "CONSTRUCT { " + entry.get("consequent") + "} WHERE { "+ entry.get("antecedent") +" FILTER NOT EXISTS { " + entry.get("consequent") + "} }' -H 'Accept:" + mime_type +"' > " + temp_file_name + output_extension)
            os.system("curl -X POST -H 'Content-Type:" + mime_type + "' --data-binary '@" + temp_file_name + output_extension + "' " + triplestore_endpoint)
        else :
            active_list.remove(axiom)
        prefixes = ""
    i += 1
os.system("rm " + temp_file_name + output_extension)
