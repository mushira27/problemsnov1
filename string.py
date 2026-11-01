class solution:
    def countDaysTogether(self,arriveAlice:str,leaveAlice:str,ariveBob:str,leaveBob:str)->int:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        def days(date):
            month, day = map(int, date.split('-'))
            return sum(months[:month-1]) + day
        arriveAlice_days = days(arriveAlice)
        leaveAlice_days = days(leaveAlice)
        arriveBob_days = days(ariveBob)
        leaveBob_days = days(leaveBob)
        # Find the overlap period
        start_overlap = max(arriveAlice_days, arriveBob_days)
        end_overlap = min(leaveAlice_days, leaveBob_days)
        # Calculate the number of days in the overlap period
        if start_overlap <= end_overlap:
            return end_overlap - start_overlap + 1
        else:
            return 0