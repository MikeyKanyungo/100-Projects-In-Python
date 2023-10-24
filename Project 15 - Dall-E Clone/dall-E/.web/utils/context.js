import { createContext } from "react"
import { Event, hydrateClientStorage } from "/utils/state.js"

export const initialState = {"complete": false, "image_url": "", "is_hydrated": false, "processing": false, "prompt": ""}
export const StateContext = createContext(null);
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {}, "local_storage": {}}
export const initialEvents = [
    Event('state.hydrate', hydrateClientStorage(clientStorage)),
]