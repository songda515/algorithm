# programmers_truck.py

"""
[스택/큐] Level2 다리를 지나는 트럭
트럭은 1초에 1만큼 움직인다.
bridge_length : 다리 길이
weight : 다리가 견딜 수 있는 무게
* 트럭이 다리에 완전히 오르지 않은 경우, 트럭의 무게는 고려하지 않는다.
"""

def solution(bridge_length, weight, truck_weights):
    on_bridge = []
    truck_count = []
    time = 1

    while(truck_weights or on_bridge):
        if truck_weights:
            total_weight = sum(on_bridge) + truck_weights[0]
            if total_weight <= weight:
                on_bridge.append(truck_weights.pop(0))
                truck_count.append(0)

        # 1초에 1만큼 이동
        for i in range(len(truck_count)):
            truck_count[i] += 1
        
        if truck_count[0] == bridge_length:
            truck_count.pop(0)
            on_bridge.pop(0)
        #print(time, on_bridge, truck_weights, truck_count)
        time += 1
    return time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10])) # return 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))