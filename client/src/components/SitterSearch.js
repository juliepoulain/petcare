import React, { useState } from "react";

function SitterSearch({ setSearch }) {
  const [searchTerm, setSearchTerm] = useState("");

  function handleChange(e) {
    const value = e.target.value;
    setSearchTerm(value);
    setSearch(value);
  }

  return (
    <div className="searchbar">
      <input
        type="text"
        id="search"
        placeholder="Search for a sitter by name, city, or zip"
        value={searchTerm}
        onChange={handleChange}
      />
    </div>
  );
}

export default SitterSearch;
