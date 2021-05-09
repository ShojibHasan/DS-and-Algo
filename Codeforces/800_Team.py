def solution(problem_numbers):
    
    output_value=0
    for i in range(problem_numbers):
        solution_input =list(map(int, input().rstrip().split()))
        if sum(solution_input)>=2:
            output_value = output_value+1
    print(output_value)
            


problem_numbers = int(input())
solution(problem_numbers)