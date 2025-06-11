# 🎨 OOP Practice Series: An Interactive Design Pattern Showcase
## 🚀 Project Overview

This project was created to bridge the gap between theoretical knowledge of OOP design patterns and practical, hands-on understanding. Instead of just reading about patterns, users can interact with them directly, see the results in real-time, and view the underlying source code that makes it all work.

### Core Features:
*   **Interactive Demos:** Each pattern has its own dedicated page with a hands-on demonstration.
*   **Code Explained:** A tab on each page reveals the full Python source code for the pattern, with clear explanations.
*   **Modern UI:** A clean, professional, and responsive user interface built with Streamlit and custom styling.
*   **Pure Python Logic:** The core OOP logic is completely decoupled from the Streamlit UI, demonstrating good software architecture.

---

## 🛠️ Design Patterns Implemented

This application currently showcases three fundamental creational and structural design patterns:

### 1. 🚗 Builder Pattern
   - **Concept:** Separate the construction of a complex object from its representation.
   - **Demo:** A "Car Builder" where you can customize the engine, wheels, and color. The application constructs the `Car` object step-by-step based on your selections.

### 2. 💻 Composite Pattern
   - **Concept:** Compose objects into tree-like structures and then work with these structures as if they were individual objects.
   - **Demo:** A "PC Configurator" where a `PC` (a composite object) is made up of individual parts like `CPU` and `GPU` (leaf objects) and other composite parts like a `Motherboard`. The total price is calculated recursively.

### 3. ☕ Decorator Pattern
   - **Concept:** Attach new behaviors or responsibilities to objects dynamically by placing them inside special "wrapper" objects.
   - **Demo:** A "Coffee Shop" where you start with a base `Coffee` and dynamically "decorate" it with add-ons like Milk, Sugar, or Whipped Cream, each altering the final cost and description.

---

## 💻 Tech Stack

This project is built with a modern, open-source stack:

*   **Core Logic:** Python 3.x
*   **Web Framework & UI:** [Streamlit](https://streamlit.io/)
*   **UI Components:**
    *   `streamlit-option-menu` for professional navigation.
    *   `streamlit-lottie` for engaging animations.
*   **Image Handling:** Pillow (PIL Fork)

---
