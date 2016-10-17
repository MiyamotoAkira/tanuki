(ns eu.twoormore.tanuki.api.handler
  (:require [liberator.core :refer [resource defresource]]
            [liberator.dev :refer [wrap-trace]]
            [ring.middleware.params :refer [wrap-params]]
            [compojure.core :refer [defroutes ANY]]))

(defresource handle-toggles []
  :allowed-methods [:get]
  :available-media-types ["application/json"]
  :handle-ok (fn [_] (format "Hello Toggle")))

(defroutes app
  (ANY "/toggles" [] (handle-toggles)))

(def handlers
  (-> app
      wrap-params
      (wrap-trace :header :ui)))
