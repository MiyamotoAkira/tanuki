(ns eu.twoormore.tanuki.e2e-test
  (:require  [clojure.test :as t]))

;;; Need to start here the api, datastore and any caching used.
;;; Should I use just the version deployed used vagrant/chef?

;;; Tests to do (not in order they must be done)

;;; login?
;;; check agent-header is passed
;;; check log is done of request
;;; check log is done of result
;;; get all toggle ids
;;; get toggle (should just use hypermedia links here?)
;;; create toggle
;;; delete toggle
;;; switch toggle
;;; add tag to toggle
;;; delete tag on toggle
;;; search toggles by tag
;;; add sub-category to toggle (dealing with different clients?)
;;; add sub-sub-category (multiple levels)
;;; add scheduler timer for toggle (different days/times when the toggle is on)
;;; add single scheduled switch on/off
;;; 
