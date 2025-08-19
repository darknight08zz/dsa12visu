from flask import Flask, render_template, request, jsonify
import json
import time
import random

app = Flask(__name__)

class ArrayVisualizer:
    def __init__(self):
        self.array = []
    
    def set_array(self, arr):
        self.array = arr[:]
        return self.array
    
    def bubble_sort_steps(self):
        arr = self.array[:]
        steps = []
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                steps.append({
                    'type': 'compare',
                    'array': arr[:],
                    'indices': [j, j + 1],
                    'message': f'Comparing {arr[j]} and {arr[j + 1]}'
                })
                
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    steps.append({
                        'type': 'swap',
                        'array': arr[:],
                        'indices': [j, j + 1],
                        'message': f'Swapped {arr[j + 1]} and {arr[j]}'
                    })
        
        steps.append({
            'type': 'complete',
            'array': arr[:],
            'indices': [],
            'message': 'Sorting complete!'
        })
        return steps
    
    def binary_search_steps(self, target):
        arr = sorted(self.array)
        steps = []
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            steps.append({
                'type': 'check',
                'array': arr,
                'left': left,
                'right': right,
                'mid': mid,
                'target': target,
                'message': f'Checking middle element {arr[mid]} at index {mid}'
            })
            
            if arr[mid] == target:
                steps.append({
                    'type': 'found',
                    'array': arr,
                    'found_index': mid,
                    'target': target,
                    'message': f'Found {target} at index {mid}!'
                })
                return steps
            elif arr[mid] < target:
                left = mid + 1
                steps.append({
                    'type': 'search_right',
                    'array': arr,
                    'left': left,
                    'right': right,
                    'target': target,
                    'message': f'{arr[mid]} < {target}, searching right half'
                })
            else:
                right = mid - 1
                steps.append({
                    'type': 'search_left',
                    'array': arr,
                    'left': left,
                    'right': right,
                    'target': target,
                    'message': f'{arr[mid]} > {target}, searching left half'
                })
        
        steps.append({
            'type': 'not_found',
            'array': arr,
            'target': target,
            'message': f'{target} not found in array'
        })
        return steps

class StackVisualizer:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
        return {
            'operation': 'push',
            'value': value,
            'stack': self.stack[:],
            'message': f'Pushed {value} onto stack'
        }
    
    def pop(self):
        if self.stack:
            value = self.stack.pop()
            return {
                'operation': 'pop',
                'value': value,
                'stack': self.stack[:],
                'message': f'Popped {value} from stack'
            }
        return {
            'operation': 'pop',
            'value': None,
            'stack': self.stack[:],
            'message': 'Stack is empty!'
        }
    
    def peek(self):
        if self.stack:
            return {
                'operation': 'peek',
                'value': self.stack[-1],
                'stack': self.stack[:],
                'message': f'Top element is {self.stack[-1]}'
            }
        return {
            'operation': 'peek',
            'value': None,
            'stack': self.stack[:],
            'message': 'Stack is empty!'
        }

class QueueVisualizer:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
        return {
            'operation': 'enqueue',
            'value': value,
            'queue': self.queue[:],
            'message': f'Enqueued {value}'
        }
    
    def dequeue(self):
        if self.queue:
            value = self.queue.pop(0)
            return {
                'operation': 'dequeue',
                'value': value,
                'queue': self.queue[:],
                'message': f'Dequeued {value}'
            }
        return {
            'operation': 'dequeue',
            'value': None,
            'queue': self.queue[:],
            'message': 'Queue is empty!'
        }

# Global instances
array_viz = ArrayVisualizer()
stack_viz = StackVisualizer()
queue_viz = QueueVisualizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/array/set', methods=['POST'])
def set_array():
    data = request.json
    arr = data.get('array', [])
    result = array_viz.set_array(arr)
    return jsonify({'array': result})

@app.route('/api/array/bubble-sort', methods=['POST'])
def bubble_sort():
    steps = array_viz.bubble_sort_steps()
    return jsonify({'steps': steps})

@app.route('/api/array/binary-search', methods=['POST'])
def binary_search():
    data = request.json
    target = data.get('target')
    steps = array_viz.binary_search_steps(target)
    return jsonify({'steps': steps})

@app.route('/api/array/generate-random', methods=['POST'])
def generate_random_array():
    data = request.json
    size = data.get('size', 10)
    max_val = data.get('max_value', 100)
    arr = [random.randint(1, max_val) for _ in range(size)]
    result = array_viz.set_array(arr)
    return jsonify({'array': result})

@app.route('/api/stack/<operation>', methods=['POST'])
def stack_operation(operation):
    if operation == 'push':
        data = request.json
        value = data.get('value')
        result = stack_viz.push(value)
    elif operation == 'pop':
        result = stack_viz.pop()
    elif operation == 'peek':
        result = stack_viz.peek()
    elif operation == 'clear':
        stack_viz.stack = []
        result = {
            'operation': 'clear',
            'stack': [],
            'message': 'Stack cleared'
        }
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    
    return jsonify(result)

@app.route('/api/queue/<operation>', methods=['POST'])
def queue_operation(operation):
    if operation == 'enqueue':
        data = request.json
        value = data.get('value')
        result = queue_viz.enqueue(value)
    elif operation == 'dequeue':
        result = queue_viz.dequeue()
    elif operation == 'clear':
        queue_viz.queue = []
        result = {
            'operation': 'clear',
            'queue': [],
            'message': 'Queue cleared'
        }
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
