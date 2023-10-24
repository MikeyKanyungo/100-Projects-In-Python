import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Center, Heading, Image, Input, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents.map((e) => ({...e})))
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {`http://localhost:8000`}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Center sx={{"width": "100%", "height": "100vh"}}>
  <VStack sx={{"padding": "2em", "shadow": "lg", "borderRadius": "lg"}}>
  <Heading>
  {`DALL-E`}
</Heading>
  <Input onBlur={(_e0) => addEvents([Event("state.set_prompt", {value:_e0.target.value})], (_e0))} placeholder={`Enter a prompt`} type={`text`}/>
  <Button isLoading={state.processing} onClick={(_e) => addEvents([Event("state.get_image", {})], (_e))} sx={{"width": "100%"}}>
  {`Generate`}
</Button>
  <Fragment>
  {isTrue(state.complete) ? (
  <Fragment>
  <Image src={state.image_url} sx={{"height": "25em", "width": "25em"}}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
</VStack>
</Center>
  <NextHead>
  <title>
  {`reflex:DALL-E`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
