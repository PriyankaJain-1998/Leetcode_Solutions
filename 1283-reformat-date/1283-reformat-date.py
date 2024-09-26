class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"jan":"01", "feb":"02", "mar":"03", "apr":"04", 
                "may":'05', "jun":"06", "jul":"07","aug":"08",
                "sep":"09", "oct":"10","nov":"11", "dec":"12"}
        date = date.lower().split()
        if date[0].endswith(('th', 'rd', 'nd', 'st')):
            date[0] = date[0][:-2]
            if len(date[0])==1: date[0] = "0"+date[0]
        return date[2]+"-"+month[date[1]]+"-"+date[0]
