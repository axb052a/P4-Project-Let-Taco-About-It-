import React, { useEffect, useState } from "react";

function Home() {
  const [tacoRecipes, setTacoRecipes] = useState([]);

  useEffect(() => {
    // Fetch taco recipes and update the state using a relative path
    fetch("http://localhost:5555/tacos")
      .then((response) => response.json())
      .then((data) => {
        console.log("Fetched taco recipes:", data);
        setTacoRecipes(data);
      })
      .catch((error) => console.error("Error fetching taco recipes:", error));
  }, []);

  return (
    <div>
      {/* Placeholder text */}
      Explore Taco Recipes
      <ul>
        {tacoRecipes.map((recipe) => (
          <li key={recipe.taco_id}>{recipe.taco_name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
