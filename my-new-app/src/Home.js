import React, { useEffect, useState } from "react";
import SearchBar from "./SearchBar";
import { SimpleGrid, Box, Text } from "@chakra-ui/react";

function Home() {
  const [tacoRecipes, setTacoRecipes] = useState([]);
  const [loading, setLoading] = useState(true); // To indicate loading state

  useEffect(() => {
    // Fetch taco recipes and update the state using a relative path
    fetch("http://localhost:5555/tacos")
      .then((response) => response.json())
      .then((data) => {
        console.log("Fetched taco recipes:", data);
        setTacoRecipes(data);
        setLoading(false); // Set loading to false once data is fetched
      })
      .catch((error) => console.error("Error fetching taco recipes:", error));
  }, []);

  // Define a handler for the search bar


  return (
    <Box as="main" mt="20">
      <SearchBar />
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
        Let's Taco Bout' it
      </Text>
      <SimpleGrid px="40" columns={4} spacing={4}>
      
      </SimpleGrid>
    </Box>
  );
}

export default Home;
