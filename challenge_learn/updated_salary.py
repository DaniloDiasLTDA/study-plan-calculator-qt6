

def update_salary(employee_salaries: dict, name: str, adjustment: float):
    if name not in employee_salaries:
        return "Funcionário não encontrado"

    novo_salario = employee_salaries[name] * (1 + adjustment)
    employee_salaries[name] = round(novo_salario, 2)

    return f"{name}: {employee_salaries[name]}"


salary = {"alice": 5000, "bob": 2344}

print(update_salary(salary, "alice", 0.23))

