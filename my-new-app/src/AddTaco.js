import React, { useState } from "react";

const AddTacoForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    taco_name: "",
    taco_description: "",
    ingredients: "",
    instructions: "",
    image: "", // Initialize "image" with an empty string
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // You can pass the formData to a function for submission, for example, onSubmit(formData).
    // You can handle the submission logic in the parent component.
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Taco Name:
        <input
          type="text"
          name="taco_name"
          value={formData.taco_name}
          onChange={handleChange}
        />
      </label>

      <label>
        Instructions:
        <input
          type="text"
          name="instructions"
          value={formData.instructions}
          onChange={handleChange}
        />
      </label>

      <label>
        Image URL:
        <input
          type="text"
          name="image"
          value={formData.image}
          onChange={handleChange}
        />
      </label>

      <label>
       Taco Type (protein):
        <input
          type="text"
          name="taco_type"
          value={formData.taco_type}
          onChange={handleChange}
        />
      </label>

      

      <button type="submit">Add Taco Recipe</button>
    </form>
  );
};

export default AddTacoForm;
