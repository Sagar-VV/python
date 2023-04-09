dict = {'apple': 2, 'banana': 3, 'almond':2 , 'beetroot': 3, 'peach': 4}

[v[0] for v in sorted(dict.items(), key=lambda k,v: v,k )]
