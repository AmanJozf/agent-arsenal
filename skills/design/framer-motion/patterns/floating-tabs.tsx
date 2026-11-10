import React, { useState } from "react";
import { motion } from "framer-motion";

interface Tab {
  id: string;
  label: string;
}

const tabs: Tab[] = [
  { id: "overview", label: "Overview" },
  { id: "analytics", label: "Analytics" },
  { id: "reports", label: "Reports" },
  { id: "settings", label: "Settings" },
];

export function FloatingTabs() {
  const [activeTab, setActiveTab] = useState(tabs[0].id);

  return (
    <div className="flex space-x-1 bg-zinc-900/60 p-1 rounded-full border border-zinc-800">
      {tabs.map((tab) => {
        const isActive = activeTab === tab.id;
        return (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`relative px-4 py-1.5 text-sm font-medium transition-colors duration-150 rounded-full ${
              isActive ? "text-white" : "text-zinc-400 hover:text-zinc-200"
            }`}
          >
            {isActive && (
              <motion.div
                layoutId="active-pill"
                className="absolute inset-0 bg-zinc-800 rounded-full border border-zinc-700/50 shadow-sm"
                transition={{ type: "spring", stiffness: 380, damping: 30 }}
              />
            )}
            <span className="relative z-10">{tab.label}</span>
          </button>
        );
      })}
    </div>
  );
}
