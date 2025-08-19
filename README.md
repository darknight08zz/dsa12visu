# DSA Visualizer

An interactive web-based tool for visualizing Data Structures and Algorithms, built with Python Flask backend and modern HTML/CSS/JavaScript frontend.

## Features

### 🔢 Arrays & Sorting
- **Interactive Array Input**: Set custom arrays or generate random ones
- **Bubble Sort Visualization**: Watch elements swap in real-time with color-coded animations
- **Binary Search**: Visual step-by-step search with left, mid, and right pointers
- **Speed Control**: Adjust animation speed from 1-10

### 📚 Stack (LIFO)
- **Push Operation**: Add elements to the top
- **Pop Operation**: Remove elements from the top
- **Peek Operation**: View top element without removing
- **Visual Stack**: Elements stack vertically with smooth animations

### 🚪 Queue (FIFO)
- **Enqueue Operation**: Add elements to the rear
- **Dequeue Operation**: Remove elements from the front
- **Visual Queue**: Elements arranged horizontally showing front-to-rear flow

## Quick Start

### Prerequisites
- Python 3.7+ installed
- pip package manager

### Installation & Setup

1. **Create project directory and files:**
```bash
mkdir dsa-visualizer
cd dsa-visualizer
mkdir templates
```

2. **Save the files:**
   - Save the backend code as `app.py`
   - Save the frontend HTML as `templates/index.html`
   - Save the requirements as `requirements.txt`

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python app.py
```

5. **Open your browser:**
   - Go to `http://localhost:5000`
   - Start visualizing!

## Project Structure
```
dsa-visualizer/
│
├── app.py              # Flask backend with API endpoints
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend with HTML, CSS, JS
└── README.md          # This file
```

## How to Use

### Arrays & Sorting
1. **Set Array**: Enter numbers separated by commas (e.g., `5,3,8,1,9`)
2. **Random Array**: Generate a random array for testing
3. **Bubble Sort**: Click to start animated sorting
4. **Binary Search**: Enter a target number and watch the search process
5. **Speed Control**: Use the slider to adjust animation speed

### Stack Operations
1. **Push**: Enter a number and click Push to add to top
2. **Pop**: Remove the top element
3. **Peek**: View the top element without removing it
4. **Clear**: Empty the entire stack

### Queue Operations
1. **Enqueue**: Enter a number and add to the rear of queue
2. **Dequeue**: Remove element from the front
3. **Clear**: Empty the entire queue

## API Endpoints

### Array Operations
- `POST /api/array/set` - Set array with custom values
- `POST /api/array/bubble-sort` - Get bubble sort animation steps
- `POST /api/array/binary-search` - Get binary search steps
- `POST /api/array/generate-random` - Generate random array

### Stack Operations
- `POST /api/stack/push` - Push element to stack
- `POST /api/stack/pop` - Pop element from stack  
- `POST /api/stack/peek` - Peek top element
- `POST /api/stack/clear` - Clear stack

### Queue Operations
- `POST /api/queue/enqueue` - Add element to queue
- `POST /api/queue/dequeue` - Remove element from queue
- `POST /api/queue/clear` - Clear queue

## Features & Design

### Modern UI/UX
- **Glassmorphism Design**: Translucent cards with blur effects
- **Gradient Backgrounds**: Beautiful color transitions
- **Smooth Animations**: CSS transitions and keyframes
- **Responsive Layout**: Works on desktop and mobile
- **Interactive Elements**: Hover effects and visual feedback

### Educational Focus
- **Step-by-step Visualization**: Clear progression through algorithms
- **Color-coded States**: Different colors for comparing, swapping, found elements
- **Descriptive Messages**: Real-time explanations of operations
- **Speed Control**: Learn at your own pace

### Technical Implementation
- **Flask Backend**: RESTful API with JSON responses
- **Modular Frontend**: Tabbed interface with separate visualizations
- **Real-time Updates**: Fetch API for seamless communication
- **Error Handling**: Graceful handling of invalid inputs

## Customization

### Adding New Algorithms
1. Create a new class in `app.py` (e.g., `MergeSortVisualizer`)
2. Add API endpoints for the new algorithm
3. Create corresponding frontend functions
4. Add a new tab in the HTML interface

### Styling Changes
- Modify CSS variables in the `<style>` section
- Update gradient colors, border radius, shadows
- Adjust animation speeds and transitions

### Algorithm Extensions
Current algorithms can be extended with:
- **Sorting**: Merge Sort, Quick Sort, Selection Sort
- **Searching**: Linear Search, Jump Search
- **Data Structures**: Binary Trees, Linked Lists, Hash Tables

## Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge

## Contributing
Feel free to extend this visualizer with:
- New algorithms and data structures
- Enhanced animations and effects
- Mobile-first responsive improvements
- Accessibility features

## License
Open source - feel free to use and modify for educational purposes.

---

**Happy Learning! 🚀** 

This DSA Visualizer makes complex algorithms easy to understand through interactive visualizations.