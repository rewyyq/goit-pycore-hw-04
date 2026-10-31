def total_salary(path: str) -> tuple:
    counter_amount_of_money = 0
    total_salary_money = 0
    try:
        with open(path, 'r') as f:
            for line in f:
                counter_amount_of_money += 1
                splitted_line = line.strip().split(',')
                splitted_line = int(splitted_line[1].rstrip('\n')) #collecting nums from list, converting to int
                total_salary_money += splitted_line
            average = total_salary_money / counter_amount_of_money
            return (total_salary_money, average)
    except (FileNotFoundError, IndexError, ZeroDivisionError, ValueError, TypeError):
        return (0, 0)