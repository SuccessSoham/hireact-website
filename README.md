# HireAct Website

A modern, visually attractive website for HireAct - Your Placement Partner

## Features

✨ **Modern Design**
- Clean, professional layout with modern CSS
- Beautiful gradients and smooth animations
- Responsive design that works on all devices
- Dark mode toggle functionality

🎨 **Visual Enhancements**
- Hero slider with multiple background images
- Smooth scroll animations
- Interactive hover effects
- Modern color scheme with CSS variables

🚀 **Interactive Features**
- Hero image slideshow with navigation controls
- Dark/light mode toggle with local storage
- Smooth scrolling navigation
- Interactive contact form with validation
- Loading animations
- Toast notifications

📱 **Responsive Design**
- Mobile-first approach
- Optimized for tablets and desktops
- Touch-friendly navigation
- Swipe gestures for mobile slider

## Directory Structure

```
HireAct website/
├── app.py                 # Flask backend application
├── env/                   # Python virtual environment
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Modern CSS styling
│   └── js/
│       └── script.js     # Interactive JavaScript
├── images/               # Website images
│   ├── logo.png         # Company logo
│   ├── hero_*.jpeg      # Hero section images
│   └── gallery_*.jpeg   # Gallery images
└── README.md            # This file
```

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Flask

### Installation & Running

1. **Navigate to the project directory**
   ```bash
   cd "C:\Hireact website"
   ```

2. **Activate the virtual environment** (if not already active)
   ```bash
   .\env\Scripts\Activate
   ```

3. **Install Flask** (if not already installed)
   ```bash
   pip install Flask
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser and visit**
   ```
   http://127.0.0.1:5000
   ```

### Alternative Running Method

You can also run the frontend directly by opening the HTML file, but running through Flask is recommended for full functionality.

## Features Overview

### 🎯 Hero Section
- Automatic slideshow with 3 hero images
- Navigation controls (previous/next)
- Touch/swipe support for mobile
- Auto-advance every 5 seconds

### 🌙 Dark Mode
- Toggle between light and dark themes
- Preference saved in local storage
- Smooth transition animations
- Animated toggle button

### 📝 Contact Form
- Client-side validation
- Visual feedback for form submission
- Email format validation
- Success/error notifications

### 🎨 Visual Effects
- Smooth scroll animations on page load
- Hover effects on cards and buttons
- Loading animation on page load
- Parallax effects
- Interactive notifications

### 📱 Mobile Optimized
- Responsive grid layouts
- Touch-friendly navigation
- Mobile-specific interactions
- Optimized font sizes and spacing

## Customization

### Colors
Edit the CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #4f46e5;
    --secondary-color: #ec4899;
    --accent-color: #f59e0b;
    /* ... more variables */
}
```

### Images
Replace images in the `images/` folder:
- `logo.png` - Company logo
- `hero_1.jpeg`, `hero_2.jpeg`, `hero_3.jpeg` - Hero section backgrounds
- `gallery_*.jpeg` - Gallery images

### Content
Edit `templates/index.html` to update:
- Company information
- Services and offerings
- Contact details
- Navigation menu items

## Browser Support

- ✅ Chrome/Chromium (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers

## Performance Features

- CSS and JS minification ready
- Optimized images
- Efficient animations using CSS transforms
- Minimal JavaScript footprint
- Fast loading times

## Development Notes

- Flask runs in debug mode for development
- Static files are served efficiently
- Template inheritance ready for expansion
- Modern JavaScript (ES6+) features used
- CSS Grid and Flexbox for layouts

---

**Developed with ❤️ for HireAct - Your Placement Partner**

For any issues or questions, please check the Flask logs in the terminal where you ran `python app.py`.
