import React from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";
import {
  FormControl,
  FormLabel,
  Input,
  Textarea,
  Button,
  Stack,
  Heading,
  Select,
  HStack,
  Box,
} from "@chakra-ui/react";

const validationSchema = yup.object().shape({
  taco_name: yup.string().required("Taco name is required"),
  image: yup.string().required("Image URL is required"),
  taco_type: yup.string().required("Taco protein type is required"),
  instructions: yup.string().required("Instructions are required"),
  time_to_cook: yup.number().required("Time to cook is required"),
  time_to_prepare: yup.number().required("Time to prepare is required"),
});

function AddTaco() {
  const handleSubmit = (formData) => {
    console.log("Form data to be submitted:", formData);

    fetch("http://localhost:5555/tacos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Response from the backend:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div>
      <Formik
        initialValues={{
          taco_name: "",
          image: "",
          taco_type: "",
          instructions: "",
          time_to_cook: "",
          time_to_prepare: "",
        }}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {() => (
          <Form>
            <Stack spacing={4} maxW={"lg"} py={4} px={6}>
              <Heading fontSize={"4xl"} textAlign={"center"}>
                Add Taco!
              </Heading>
              <Box rounded={"lg"} bg={"white"} boxShadow={"lg"} p={8}>
                <FormControl id="taco_name" isRequired>
                  <FormLabel>Taco Name</FormLabel>
                  <Input type="text" name="taco_name" />
                </FormControl>
                <FormControl id="image" isRequired>
                  <FormLabel>Image URL</FormLabel>
                  <Input type="text" name="image" />
                </FormControl>
                <HStack>
                  <FormControl id="time_to_prepare" isRequired>
                    <FormLabel>Time to Prepare</FormLabel>
                    <Input type="number" name="time_to_prepare" />
                  </FormControl>
                  <FormControl id="time_to_cook" isRequired>
                    <FormLabel>Time to Cook</FormLabel>
                    <Input type="number" name="time_to_cook" />
                  </FormControl>
                </HStack>
                <FormControl id="taco_type" isRequired>
                  <FormLabel>Taco Type</FormLabel>
                  <Select type="text" name="taco_type">
                    <option value="Beef">Beef</option>
                    <option value="Chicken">Chicken</option>
                    <option value="Vegetarian">Vegetarian</option>
                  </Select>
                </FormControl>
                <FormControl id="instructions" isRequired>
                  <FormLabel>Instructions</FormLabel>
                  <Textarea name="instructions" />
                </FormControl>
                <Button
                  type="submit"
                  loadingText="Submitting"
                  size="lg"
                  bg={"orange.400"}
                  color={"white"}
                  _hover={{
                    bg: "orange.500",
                  }}
                >
                  Add Taco
                </Button>
              </Box>
            </Stack>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default AddTaco;
