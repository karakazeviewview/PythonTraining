scores={'network':60,'database':80,'security':50}
print(scores)
print(scores['database'])
scores['programing']=65
scores['security']=55
print(scores)
"""
Map<String,Integer>map=new HashMap<>();
map.put("network",60);
"""
del scores['security']
print(scores)
print(sum(scores.values()));
