import requests
import json

url = 'http://qainterview.cogniance.com/candidates'
name = 'Marian Shun'
position = 'QA Intern'

class ListCandidate:
    def get(self):
        res_cands = requests.get(url)
        return res_cands

class Candidate:
    def get(self, cid):
        res_cand = requests.get(url+r'/'+str(cid))
        return res_cand
    
    def post(self, name, position):
        data={'name': name, 
               'position': position}
        res_new_cand = requests.post(url, 
                                     headers={'content-type': 'application/json'},
                                     
                                     data=json.dumps(data) )
        return res_new_cand
    
    def post_without_headers(self, name, position):
        data={'name': name, 
               'position': position}
        res_new_cand = requests.post(url, 
                                     
                                     
                                     data=json.dumps(data) )
        return res_new_cand
    
    def post_bad_body_with_two_names(self, name, name2, position):
        data={'name' 'name': name, 
               'position': position}
        res_new_cand = requests.post(url, 
                                     headers={'content-type': 'application/json'},

                                     
                                     data=json.dumps(data) )
        return res_new_cand
        
    def post_bad_body_without_name(self, position):
        data={'position': position}
        res_new_cand = requests.post(url, 
                                     headers={'content-type': 'application/json'},

                                     
                                     data=json.dumps(data) )
        return res_new_cand
        
    def post_bad_body(self, position, name, id):
        data={'pos': position,
        'nam': name, 
        'id': id,
        }
        res_new_cand = requests.post(url, 
                                     headers={'content-type': 'application/json'},

                                     
                                     data=json.dumps(data) )
        return res_new_cand
        
    def post_with_bad_url(self, badurl):
        data={'name': name, 
               'position': position}
        res_new_cand = requests.post(badurl, 
                                     headers={'content-type': 'application/json'},
                                     
                                     data=json.dumps(data) )
        return res_new_cand
    
    def delete(self, delid):
        del_cands = requests.delete(url+r'/'+str(delid))
        return del_cands
