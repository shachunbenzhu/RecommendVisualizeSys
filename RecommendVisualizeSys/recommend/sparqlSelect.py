from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

def getInitResult() :
    name = "月球"
    sparql.setQuery("""
           PREFIX dbo: <http://dbpedia.org/ontology/>
        	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        	PREFIX dct: <http://purl.org/dc/terms/>

        	SELECT distinct ?movie ?name ?subject ?thumnail ?abstract
            WHERE
            {
                ?movie rdf:type dbo:Film.
                ?movie rdfs:label ?name.
                ?movie dbo:abstract ?abstract.
                OPTIONAL{
        			?movie dbo:thumbnail ?thumnail.
                } 
                ?movie dct:subject ?subject.
                FILTER(REGEX(?name,"%s","i")).
            } 
            ORDER BY DESC(?movie)
            limit 5
        """ % name)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def getSelectResult(search_type, search_condition) :
    if search_type == "作者":
        sparql.setQuery("""
                   PREFIX dbo: <http://dbpedia.org/ontology/>
                	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                	PREFIX dct: <http://purl.org/dc/terms/>

                	SELECT distinct ?movie ?name ?subject ?thumnail ?abstract
                    FROM <http://en.dbpedia.org>
                    WHERE
                    {
                        ?movie rdf:type dbo:Film.
                        ?movie dbo:director ?author.
                        FILTER(REGEX(?author,"%s","i")).
                        ?movie rdfs:label ?name.
                        FILTER(REGEX(?name,"月球","i")).
                        ?movie dbo:abstract ?abstract.
                        OPTIONAL{
                			?movie dbo:thumbnail ?thumnail.
                		} 
                        ?movie dct:subject ?subject.
                    } 
                    ORDER BY DESC(?movie)
                    limit 5
                """%search_condition)
    elif search_type == "类型":
        if search_condition == "请选择...":
            results = getInitResult()
            return results
        elif search_condition == "图书":
            search_condition = "dbo:Book"
        elif search_condition == "游戏":
            search_condition = "dbo:Game"
        else:
            search_condition = "dbo:Film"
        sparql.setQuery("""
                           PREFIX dbo: <http://dbpedia.org/ontology/>
                        	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        	PREFIX dct: <http://purl.org/dc/terms/>

                        	SELECT distinct ?movie ?name ?subject ?thumnail ?abstract
                            FROM <http://en.dbpedia.org>
                            WHERE
                            {
                                ?movie rdf:type ?type.
                                FILTER(REGEX(?type,"%s","i")).
                                ?movie rdfs:label ?name.
                                FILTER(REGEX(?name,"月球","i")).
                                ?movie dbo:abstract ?abstract.
                                OPTIONAL{
                        			?movie dbo:thumbnail ?thumnail.
                        		} 
                                ?movie dct:subject ?subject.
                            } 
                            ORDER BY DESC(?movie)
                            limit 5
                        """ % search_condition)
    else:
        sparql.setQuery("""
                           PREFIX dbo: <http://dbpedia.org/ontology/>
                        	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        	PREFIX dct: <http://purl.org/dc/terms/>

                        	SELECT distinct ?movie ?name ?subject ?thumnail ?abstract
                            WHERE
                            {
                                ?movie rdf:type dbo:Film.
                                ?movie rdfs:label ?name.
                                FILTER(REGEX(?name,"月球","i")).
                                ?movie dbo:abstract ?abstract.
                                OPTIONAL{
                        			?movie dbo:thumbnail ?thumnail.
                        		} 
                                ?movie dct:subject ?subject.
                                FILTER(REGEX(?subject,"%s","i")).
                            } 
                            ORDER BY DESC(?movie)
                            limit 5
                        """ %search_condition)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


def getFilmResult() :
    name = "月球"
    sparql.setQuery("""
           PREFIX dbo: <http://dbpedia.org/ontology/>
        	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        	PREFIX dct: <http://purl.org/dc/terms/>

        	SELECT distinct ?movie ?name ?subject ?thumnail ?abstract
            WHERE
            {
                ?movie rdf:type dbo:Film.
                ?movie rdfs:label ?name.
                FILTER(REGEX(?name,"%s","i")).
            } 
            ORDER BY DESC(?movie)
            limit 5
        """ % name)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def getBookResult() :
    name = "月球"
    sparql.setQuery("""
           PREFIX dbo: <http://dbpedia.org/ontology/>
        	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        	PREFIX dct: <http://purl.org/dc/terms/>

        	SELECT distinct ?book ?name
            WHERE
            {
                ?book rdf:type dbo:Book.
                ?book rdfs:label ?name.
                FILTER(REGEX(?name,"%s","i")).
            } 
            ORDER BY DESC(?movie)
            limit 5
        """ % name)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def getGameResult() :
    name = "月球"
    sparql.setQuery("""
           PREFIX dbo: <http://dbpedia.org/ontology/>
        	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        	PREFIX dct: <http://purl.org/dc/terms/>

        	SELECT distinct ?game ?name
            WHERE
            {
                ?game rdf:type dbo:Game.
                ?game rdfs:label ?name.
                FILTER(REGEX(?name,"%s","i")).
            } 
            ORDER BY DESC(?movie)
            limit 5
        """ % name)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results