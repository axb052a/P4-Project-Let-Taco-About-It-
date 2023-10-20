import React, { useState } from "react";
import {
  Card,
  Box,
  Image,
  Stack,
  Heading,
  Text,
  Center,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
  Button,
} from "@chakra-ui/react";
import {
  ExternalLinkIcon, // You can remove this import if not needed
} from "@chakra-ui/icons";

export default function TacoCard({
  name,
  image,
  user,
  displayUser,
  tacoType,
  instructions,
  timeToCook,
  timeToPrepare,
  onClick, // Add the onClick handler for the "Instructions" button
}) {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleOpenModal = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      <Card position="relative" height="400px" width="300px">
        <Center>
          <Box
            style={{
              width: "100%",
              height: "100%",
              position: "absolute",
              top: 0,
              left: 0,
              backfaceVisibility: "hidden",
              display: "block",
            }}
          >
            <Image
              src={
                image.startsWith("http") || image.startsWith("https")
                  ? image
                  : `http://localhost:5555/${image}` // Fixed the template string
              }
              alt={name}
              borderRadius="lg"
              boxSize="xs"
              objectFit="cover"
            />
            <Stack mt="4" spacing="3" textAlign="center">
              <Heading size="md">{name}</Heading>
              {displayUser ? <Text>Added by @{user}</Text> : ""}
              <Button
                onClick={handleOpenModal}
                colorScheme="blue"
                leftIcon={<ExternalLinkIcon />} // Add this icon if needed
              >
                View Details
              </Button>
            </Stack>
          </Box>
        </Center>
      </Card>

      <Modal isOpen={isModalOpen} onClose={handleCloseModal}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>{name}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Stack spacing="4">
              
              <Text>Instructions: {instructions}</Text>
              <Text>Time to Cook: {timeToCook} minutes</Text>
              <Text>Time to Prepare: {timeToPrepare} minutes</Text>
            
            </Stack>
          </ModalBody>
          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={handleCloseModal}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}
