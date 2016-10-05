(defproject eu.twoormore.tanuki.api "0.1.0-SNAPSHOT"
  :description "Api for the Tanuki tool"
  :url "http://example.com/FIXME"
  :license {:name "MIT License"
            :url ""}
  :plugins [[cider/cider-nrepl "0.13.0"]
            [lein-ring "0.9.7"]
            [refactor-nrepl "2.2.0"]]
  :ring {:handler appointment.handler/handlers
         :nrepl {:start? true}}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [liberator "0.14.1"]
                 [compojure "1.5.1"]
                 [ring/ring-core "1.5.0"]])
