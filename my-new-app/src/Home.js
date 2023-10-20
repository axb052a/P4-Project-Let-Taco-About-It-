import React, { useEffect, useState } from "react";
import SearchBar from "./SearchBar";
import { SimpleGrid, Box, Text } from "@chakra-ui/react";
import { Link } from "react-router-dom";
import TacoCard from "./TacoCard";

function Home() {
  const [tacoRecipes, setTacoRecipes] = useState([]);
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(true); // To indicate loading state

  useEffect(() => {
    // Fetch taco recipes and update the state using a relative path
    fetch("http://localhost:5555/tacos")
      .then((response) => response.json())
      .then((data) => {
        console.log("Fetched taco recipes:", data);
        setTacoRecipes(data);
        setSearchResults(data);
        setLoading(false); // Set loading to false once data is fetched
      })
      .catch((error) => console.error("Error fetching taco recipes:", error));
  }, []);

  // Define a handler for the search bar

 const handleSearch = (searchTerm) => {
   if (!searchTerm || searchTerm.trim() === "") {
     // If the search input is empty, display all taco recipes
     setSearchResults(tacoRecipes);
   } else {
     // Filter taco recipes based on the search term (case-insensitive)
     setSearchResults(
       tacoRecipes.filter(
         (taco) =>
           !taco.taco_name.toLowerCase().includes("example") &&
           taco.taco_name.toLowerCase().includes(searchTerm.toLowerCase())
       )
     );
   }
 };


  return (
    <Box as="main" mt="20">
      <SearchBar onSearch={handleSearch} />
      <Text
        lineHeight="1.2"
        fontWeight="bold"
        fontSize="56px"
        color="Gray.500"
        maxWidth="100%"
        mb="20"
        textAlign="center"
        mt="10"
      >
        Let's Taco Bout These ....
      </Text>
      <SimpleGrid px="40" columns={4} spacing={4}>
        {searchResults
          .filter((taco) => !taco.taco_name.toLowerCase().includes("example"))
          .sort((a, b) => b.timestamp - a.timestamp) // Sort by timestamp in descending order
          .map((taco) => (
            <TacoCard
              name={taco.taco_name}
              image={taco.image}
              instructions={taco.instructions}
              timeToCook={taco.time_to_cook}
              timeToPrepare={taco.time_to_prepare}
            />
          ))}
      </SimpleGrid>
    </Box>
  );}

export default Home;