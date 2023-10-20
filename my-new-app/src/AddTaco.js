import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";
import {
  FormControl,
  FormLabel,
  Input,
  Select,
  Button,
  Text,
} from "@chakra-ui/react";

const validationSchema = yup.object().shape({
  taco_name: yup.string().required("Taco name is required"),
  image: yup.string().required("Image URL is required"),
  taco_type: yup.string().required("Taco protein type is required"),
  instructions: yup.string().required("Instructions are required"),
  time_to_cook: yup.number().required("Time to cook is required"),
  time_to_prepare: yup.number().required("Time to prepare is required"),
});

function AddTaco({ setRefreshPage }) {
  const [successMessage, setSuccessMessage] = useState("");
  const formik = useFormik({
    initialValues: {
      taco_name: "",
      image: "",
      taco_type: "",
      instructions: "",
      time_to_cook: "",
      time_to_prepare: "",
    },
    validationSchema: validationSchema,
    onSubmit: (values) => {
      fetch("http://localhost:5555/tacos", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      }).then((response) => {
        if (response.status === 201) {
          setRefreshPage((prev) => !prev);
          setSuccessMessage("Taco added successfully.");
        }
      });
    },
  });

  return (
    <div>
      {successMessage && <Text color="green">{successMessage}</Text>}
      <form onSubmit={formik.handleSubmit} style={{ margin: "30px" }}>
        <FormControl id="taco_name" isRequired>
          <FormLabel>Taco Name</FormLabel>
          <Input
            type="text"
            name="taco_name"
            value={formik.values.taco_name}
            onChange={formik.handleChange}
          />
          {formik.errors.taco_name && (
            <Text color="red">{formik.errors.taco_name}</Text>
          )}
        </FormControl>

        <FormControl id="image" isRequired>
          <FormLabel>Image URL</FormLabel>
          <Input
            type="text"
            name="image"
            value={formik.values.image}
            onChange={formik.handleChange}
          />
          {formik.errors.image && (
            <Text color="red">{formik.errors.image}</Text>
          )}
        </FormControl>

        <FormControl id="time_to_prepare" isRequired>
          <FormLabel>Time to Prepare</FormLabel>
          <Input
            type="number"
            name="time_to_prepare"
            value={formik.values.time_to_prepare}
            onChange={formik.handleChange}
          />
          {formik.errors.time_to_prepare && (
            <Text color="red">{formik.errors.time_to_prepare}</Text>
          )}
        </FormControl>

        <FormControl id="time_to_cook" isRequired>
          <FormLabel>Time to Cook</FormLabel>
          <Input
            type="number"
            name="time_to_cook"
            value={formik.values.time_to_cook}
            onChange={formik.handleChange}
          />
          {formik.errors.time_to_cook && (
            <Text color="red">{formik.errors.time_to_cook}</Text>
          )}
        </FormControl>

        <FormControl id="taco_type" isRequired>
          <FormLabel>Taco Type</FormLabel>
          <Select
            name="taco_type"
            value={formik.values.taco_type}
            onChange={formik.handleChange}
          >
            <option value="Beef">Beef</option>
            <option value="Chicken">Chicken</option>
            <option value="Vegetarian">Vegetarian</option>
          </Select>
          {formik.errors.taco_type && (
            <Text color="red">{formik.errors.taco_type}</Text>
          )}
        </FormControl>

        <FormControl id="instructions" isRequired>
          <FormLabel>Instructions</FormLabel>
          <Input
            as="textarea"
            name="instructions"
            value={formik.values.instructions}
            onChange={formik.handleChange}
          />
          {formik.errors.instructions && (
            <Text color="red">{formik.errors.instructions}</Text>
          )}
        </FormControl>

        <Button type="submit">Add Taco</Button>
      </form>
    </div>
  );
}

export default AddTaco;
