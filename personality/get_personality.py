import sqlite3

from watson_developer_cloud import PersonalityInsightsV3

import re 

class Personality:
    def __init__(self, text):
        self.text = text
        

    def create_trait_plots(self, traits):
        result = {trait['name']: trait['percentile'] for trait in traits}
        return result
    
    def ibm_watson_data(self):
        url = 'https://api.eu-gb.personality-insights.watson.cloud.ibm.com/instances/18ed6fd4-cb1d-4ec2-954e-29b8934ca84c'
        apikey = 'jtwt-9a5t51pF3hGTPcNN6r8FkrtZsdDlFPxyW-_PBQT'
        service = PersonalityInsightsV3(url=url , iam_apikey=apikey , version='2017-10-13' )
        if len(re.findall('\w+', self.text)) > 150:
            data = service.profile(self.text, content_type='text/plain').get_result()
            result_needs = {need['name']:need['percentile'] for need in data['needs']}
            result_values = self.create_trait_plots(data['values'])
            result_personality = self.create_trait_plots(data['personality'])
            result_personality_child = [self.create_trait_plots(big5['children']) for big5 in data['personality']]
            return {
                'result_needs': result_needs,
                'result_values': result_values,
                'result_personality': result_personality,
                'result_personality_child': result_personality_child
            }
    
#      This data is return from IBM Watson
#     'Openness': 0.9958692431556619, 
#     'Conscientiousness': 0.4188948461834662, 
#     'Extraversion': 0.20585797305903053, 
#     'Agreeableness': 0.013937162182467044, 
#     'Emotional range': 0.1549736067837315
