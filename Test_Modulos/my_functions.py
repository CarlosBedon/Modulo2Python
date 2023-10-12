def get_totals(orders):
    answer = [order['total'] for order in orders]
    print(answer)
    return answer

def calc_total(totals):
   print(sum(totals))
   return sum(totals)