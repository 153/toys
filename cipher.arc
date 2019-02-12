;;;; DIANA symmetric polyalphabetic cipher
;;;; (encode-string "helloworld" "key") => "IRQHHSAUSI"
;;;; (decode-string "IRQHHSAUSI" "key") => "HELLOWORLD"
;;;;
;;;; Online interpreter:
;;;; https://arclanguage.github.io/rainbow-js/test/#libs

(= letter? (fn (text) (< 64 (coerce text 'int) 91)))
(= formatstr (fn (text) (keep letter? (upcase text))))
(= getpos (fn (text) (- (coerce (text 0) 'int) 65)))
(= encode (fn (pt ct) (string (coerce (+ 65
  (mod (- 25 (getpos pt) (getpos ct)) 26)) 'char ))))

(= encode-message (fn (pt k)
  (= pt (formatstr pt))
  (= k (formatstr k))
  (= op "")
  (when (> (len pt) (len k))
    (= k (string k pt)))
  (for i 0 (- (len pt) 1)
    (= op (string op (encode (string (pt i)) (string (k i))))))
  op))
    
(= decode-message (fn (ct k)
  (= ct (formatstr ct))
  (= k (formatstr k))
  (while (< (len k) (len ct))
    (for i 0 (- (len ct) 1)
      (= k (string k (encode (string (k i)) (string (ct i)))))))
  (encode-message ct k)))
