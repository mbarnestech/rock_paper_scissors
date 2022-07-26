def return_day(num):
        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        numdaydict = {i:day[i-1] for i in range(1,8)}
        return numdaydict.get(num)
print(return_day(3))