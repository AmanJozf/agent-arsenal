# Framer Motion: Universal Agent Animation Instructions

These instructions guide any AI coding agent (Claude Code, Cursor, Antigravity, OpenCode, Codex) to build fluid, high-performance 60fps animations in React and Next.js using Framer Motion (`motion/react`).

---

## 🎯 Role & Objective
You are a senior motion design engineer. When implementing transitions, gestures, or scroll animations:
1. Use GPU-accelerated properties (`opacity`, `scale`, `x`, `y`, `rotate`). Never animate layout properties like `height`, `width`, `top`, or `margin` unless using `layout` or `layoutId`.
2. Prefer organic spring physics over stiff linear easing.
3. Always support accessibility by checking `useReducedMotion()`.

---

## 🛠️ Core Presets & Patterns

### 1. Spring Physics Presets
```tsx
// Snappy Micro-Interactions (buttons, toggles, icons)
export const snappySpring = { type: "spring", stiffness: 400, damping: 25 };

// Smooth Content Transitions (cards, modals, page reveals)
export const smoothSpring = { type: "spring", stiffness: 260, damping: 20, mass: 0.8 };

// Gentle Floating (ambient glow, floating badges)
export const gentleSpring = { type: "spring", stiffness: 120, damping: 14 };
```

### 2. Smooth Shared Layout Morphing (`layoutId`)
When creating tab indicators or expanding cards:
```tsx
{isActive && (
  <motion.div
    layoutId="active-pill"
    className="absolute inset-0 bg-primary rounded-full -z-10"
    transition={{ type: "spring", stiffness: 350, damping: 30 }}
  />
)}
```

### 3. Exit Animations (`AnimatePresence`)
```tsx
<AnimatePresence mode="wait">
  {isOpen && (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      transition={{ duration: 0.15, ease: [0.16, 1, 0.3, 1] }}
    >
      {content}
    </motion.div>
  )}
</AnimatePresence>
```

### 4. Scroll-Driven Transitions
Use `useScroll` and `useTransform` for parallax and scroll progress:
```tsx
const { scrollYProgress } = useScroll({ target: containerRef, offset: ["start end", "end start"] });
const opacity = useTransform(scrollYProgress, [0, 0.3, 0.8, 1], [0, 1, 1, 0]);
const y = useTransform(scrollYProgress, [0, 1], [40, -40]);
```

---

## ⚡ Direct Prompt Template

```text
Add smooth animations using Framer Motion:
Use layoutId for the active tab pill, snappy spring physics for card hovers,
and AnimatePresence with mode="wait" for view transitions.
```
