(ns eu.twoormore.tanuki.api)

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))

(defroutes apply (ANY "/toggles" [] handle-toggles))

(def handlers
  (-> app))
