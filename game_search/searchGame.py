from elasticsearch import Elasticsearch

es = Elasticsearch()

def search_game(query_text):
    res = es.search(
        index = 'games',
        size = 100,
        body = {
            "query": {
                "function_score": {
                    "query": {
                        "multi_match": {
                            "query": query_text,
                            "fields": ['Name^2', 'Platform^1', 'Genre^1', 'Publisher^1'],
                            "type": "most_fields"
                        },
                    },
                    "functions": [{
                        "field_value_factor": {
                            "field": "Game_Score",
                        },
                    }],
                    "boost_mode": "sum"
                }
            }
        }
    )

    ret = []

    for hit in res['hits']['hits']:
        ret.append({
            'name': hit['_source']['Name'],
            'platform': hit['_source']['Platform'],
            'publisher': hit['_source']['Publisher'],
            'year': int(hit['_source']['Year_of_Release']),
            'genre': hit['_source']['Genre'],
            'sales': hit['_source']['Global_Sales'],
            'user_count': int(hit['_source']['User_Count']),
            'user_score': hit['_source']['User_Score'],
            'critic_count': int(hit['_source']['Critic_Count']),
            'critic_score': hit['_source']['Critic_Score'],
        })
    
    return ret