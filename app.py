import streamlit as st
import json
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image, ImageDraw, ImageFont

# Import our OOP classes
from core.decorator import Coffee, WithMilk, WithSugar, WithWhippedCream
from core.builder import SportsCarBuilder
from core.composite import LeafPart, CompositePart

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="OOP Practice Series",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- HELPER FUNCTIONS ---
def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError: return None

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_code(file_path):
    with open(file_path) as f:
        st.code(f.read(), language="python")

def create_placeholder_image(width=600, height=400, text="Car Image Here"):
    img = Image.new('RGB', (width, height), color=(200, 200, 200))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()
    textwidth, textheight = d.textsize(text, font)
    x, y = (width - textwidth) / 2, (height - textheight) / 2
    d.text((x, y), text, fill=(100, 100, 100), font=font)
    return img

# --- LOAD ASSETS & STYLES ---
load_css("assets/style.css") # We can keep the CSS file for future global styles if needed.
lottie_build = load_lottiefile("assets/build_animation.json")


# --- SIDEBAR WITH NEW COOL THEME ---
with st.sidebar:
    st.title("🎨 OOP Patterns in Python")
    st.markdown("---")
    selected = option_menu(
        menu_title=None,
        options=["Builder", "Composite", "Decorator"],
        icons=["gear-fill", "diagram-3-fill", "palette-fill"],
        # ### NEW COOL BLUE THEME FOR SIDEBAR ###
        styles={
            "container": {"padding": "0!important", "background-color": "#262730"}, # Dark background
            "icon": {"color": "#63d4ee", "font-size": "22px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin":"0px",
                "color": "#fafafa", # Light text for dark background
                "--hover-color": "#3a3c49"
            },
            "nav-link-selected": {"background-color": "#02abde"}, # Cool blue for selection
        }
    )
    st.markdown("---")
    st.info("This app interactively demonstrates key OOP design patterns. Select a pattern to see it in action and view the source code.")
    st.markdown(
        """<div style='text-align: center; margin-top: 20px;'>
        Created with ❤️ by <strong>Taha</strong>
        </div>""", unsafe_allow_html=True
    )

# --- MAIN PAGE CONTENT ---

# ==============================================================================
# --- BUILDER PATTERN PAGE (FIXED) ---
# ==============================================================================
if selected == "Builder":
    st.title("🚗 The Builder Pattern")
    st.markdown("""
    **Concept:** The Builder pattern separates the construction of a complex object from its representation,
    so that the same construction process can create different representations. It's ideal when an object
    has many configuration options.
    """)
    st.markdown("---")

    tab1, tab2 = st.tabs(["**Interactive Demo**", "**Code & Explanation**"])

    with tab1:
        # NOTE: The st.container() and extra markdown divs are completely removed.
        col1, col2 = st.columns([1, 1.5], gap="large")

        with col1:
            st.subheader("1. Customize Your Options")
            builder = SportsCarBuilder()
            engine = st.selectbox("Engine", ["V6 Turbo", "V8 Supercharged", "Electric Motor"])
            wheels = st.radio("Wheels", ["18-inch Alloy", "19-inch Carbon Fiber", "20-inch Chrome"])
            color = st.color_picker("Color", "#EFEFEF", help="Choose a light color for better visibility")

            if st.button("Build My Car!", key="build_car", use_container_width=True):
                car = builder.set_engine(engine).set_wheels(wheels).set_color(color).get_car()
                st.session_state.car = car
                st.balloons()
        
        with col2:
            st.subheader("2. See Your Final Product")
            if 'car' in st.session_state:
                car_specs = st.session_state.car
                st.success("Your custom car has been built!")
                
                try:
                    image = Image.open('assets/car_template.png')
                    if image.size == (0,0): raise ValueError("Image is empty")
                except (FileNotFoundError, ValueError, Image.UnidentifiedImageError):
                    image = create_placeholder_image()

                # FIXED the st.image warning parameter
                st.image(image, use_column_width='auto', caption="Your configured car")
                
                hex_color_int = int(car_specs.color.lstrip('#'), 16)
                text_color = 'black' if hex_color_int > 0x888888 else 'white'
                st.markdown(f"""
                <div style="background-color: {car_specs.color}; padding: 10px; border-radius: 8px; text-align: center; margin-top: 10px; border: 1px solid #ccc;">
                    <strong style="color: {text_color}; text-shadow: 1px 1px 2px #555;">Selected Color: {car_specs.color}</strong>
                </div>
                """, unsafe_allow_html=True)

                st.code(str(car_specs), language="text")
            else:
                st.info("Your configured car will appear here once you build it.")

    with tab2:
        st.header("Code Explained: Builder Pattern")
        st.markdown("""
        The pattern has three main parts:
        1.  **Product (`Car`):** The complex object we want to build.
        2.  **Builder (`CarBuilder`):** An abstract interface for creating the parts of the Product.
        3.  **Concrete Builder (`SportsCarBuilder`):** Implements the Builder interface to construct and assemble the parts of the product.
        """)
        show_code("core/builder.py")

# ==============================================================================
# --- COMPOSITE PATTERN PAGE (FIXED) ---
# ==============================================================================
elif selected == "Composite":
    st.title("💻 The Composite Pattern")
    st.markdown("""
    **Concept:** The Composite pattern allows you to compose objects into tree-like structures and then
    work with these structures as if they were individual objects.
    """)
    st.markdown("---")

    tab1, tab2 = st.tabs(["**Interactive Demo**", "**Code & Explanation**"])

    with tab1:
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.subheader("Select Components")
            add_cpu = st.checkbox("🧠 CPU (Intel i9) - $500", value=True)
            add_ram = st.checkbox("💾 RAM (32GB DDR5) - $150", value=True)
            add_gpu = st.checkbox("🎮 GPU (NVIDIA RTX 4080) - $1200", value=True)
            add_storage = st.checkbox("💽 SSD (2TB NVMe) - $200", value=True)

        pc_case = CompositePart("PC Case", 100)
        motherboard = CompositePart("Motherboard", 300)
        pc_case.add_part(motherboard)
        if add_cpu: motherboard.add_part(LeafPart("CPU (Intel i9)", 500))
        if add_ram: motherboard.add_part(LeafPart("RAM (32GB DDR5)", 150))
        if add_gpu: pc_case.add_part(LeafPart("GPU (NVIDIA RTX 4080)", 1200))
        if add_storage: pc_case.add_part(LeafPart("SSD (2TB NVMe)", 200))

        with col2:
            st.subheader("Your Configuration Total")
            total_price = pc_case.get_price()
            st.metric(label="Total PC Price", value=f"${total_price:,.2f}")
            with st.expander("Show Price Breakdown"):
                st.write(f"🖥️ PC Case: ${pc_case.price}")
                st.write(f"🕹️ Motherboard: ${motherboard.price}")
                for part in motherboard._sub_parts: st.write(f"    L-- {part.name}: ${part.price}")
                for part in pc_case._sub_parts:
                    if isinstance(part, LeafPart): st.write(f"🖥️ {part.name}: ${part.price}")

    with tab2:
        st.header("Code Explained: Composite Pattern")
        st.markdown("""
        The key idea is a shared interface:
        1.  **Component (`Part`):** An abstract class that declares the interface for both simple and complex objects.
        2.  **Leaf (`LeafPart`):** Represents the individual, end-node objects of the composition.
        3.  **Composite (`CompositePart`):** Represents objects that can have children. Its methods typically delegate the work to its children.
        """)
        show_code("core/composite.py")

# ==============================================================================
# --- DECORATOR PATTERN PAGE (FIXED) ---
# ==============================================================================
elif selected == "Decorator":
    st.title("☕ The Decorator Pattern")
    st.markdown("""
    **Concept:** The Decorator pattern allows you to attach new behaviors to objects
    dynamically by placing them inside special "wrapper" objects.
    """)
    st.markdown("---")

    tab1, tab2 = st.tabs(["**Interactive Demo**", "**Code & Explanation**"])

    with tab1:
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.subheader("Choose Your Add-ons")
            if lottie_build: st_lottie(lottie_build, height=150, key="coffee")
            add_milk = st.checkbox("🥛 Add Milk (+$2)")
            add_sugar = st.checkbox("🍬 Add Sugar (+$1)")
            add_whipped_cream = st.checkbox("🍦 Add Whipped Cream (+$3)")
            
        my_coffee = Coffee()
        if add_milk: my_coffee = WithMilk(my_coffee)
        if add_sugar: my_coffee = WithSugar(my_coffee)
        if add_whipped_cream: my_coffee = WithWhippedCream(my_coffee)

        with col2:
            st.subheader("Your Final Order")
            final_description = my_coffee.get_description()
            final_cost = my_coffee.get_cost()
            st.info(f"**Description:** `{final_description}`")
            st.success(f"**Total Cost:** `${final_cost:.2f}`")
            st.markdown("---")
            st.subheader("How It's Built Dynamically:")
            st.code(f"""
# 1. Start with a base object
coffee = Coffee() 

# 2. Dynamically wrap it with decorators
{'coffee = WithMilk(coffee)' if add_milk else '# Milk not added'}
{'coffee = WithSugar(coffee)' if add_sugar else '# Sugar not added'}
{'coffee = WithWhippedCream(coffee)' if add_whipped_cream else '# Whipped Cream not added'}

# 3. The final object has new behavior!
coffee.get_cost() # Returns -> {final_cost}
""", language="python")

    with tab2:
        st.header("Code Explained: Decorator Pattern")
        st.markdown("""
        The structure involves:
        1.  **Component (`Coffee`):** The interface for objects that can have responsibilities added.
        2.  **Concrete Decorators (`WithMilk`, etc.):** These are the "wrappers" that add their own behavior.
        """)
        show_code("core/decorator.py")