import React, { useState } from "react";
import { Input, Box } from "@chakra-ui/react";

export default function SearchBar({ onSearch }) {
  const [search, setSearch] = useState("");

  const handleSearchChange = (event) => {
    setSearch(event.target.value);
    onSearch(event.target.value);
  };

  return (
    <Box
      position="relative"
      bgImage="url('https://images.everydayhealth.com/images/creative-taco-recipes-bursting-with-nutrition-00-722x406.jpg?w=720')"
      bgSize="cover"
      bgPosition="center"
      minHeight="30vw" 
      display="flex" 
      justifyContent="center"
      alignItems="center"
    >
      <Box
        bg="white" // Set the background color of the search bar
        maxWidth="1000px" // Set a maximum width for the search bar
        width="100%" // Make the search bar take up the entire width of the container
        borderRadius="md" // Add some border radius for styling
        boxShadow="md" // Add a box shadow for a lifted appearance
      >
        <Input
          type="text"
          value={search}
          onChange={handleSearchChange}
          placeholder="Search for taco..."
          focusBorderColor="orange.300"
          color="orange.500"
          _placeholder={{ color: "inherit" }}
          bg="white" // Set the background color of the input to match the container
        />
      </Box>
    </Box>
  );
}
