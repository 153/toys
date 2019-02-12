;; Diana explained   : https://rijmenants.blogspot.com/2017/10/a-fast-reciprocal-one-time-pad-table.html
;; Online interpreter: https://arclanguage.github.io/rainbow-js/test/#libs

(= letter? (fn (text) (< 64 (coerce text 'int) 91)))
(= formatstr (fn (text) (keep letter? (upcase text))))
(= getpos (fn (text) (- (coerce (text 0) 'int) 65)))
(= encode (fn (pt ct) (string (coerce (+ 65 (mod (- 25 (getpos pt) (getpos ct)) 26)) 'char ))))

(= encode-string (fn (pt k)
   (= pt (formatstr pt))
   (= k (formatstr k))
   (= op "")
   (if (> (len pt) (len k)) (= k (formatstr (string k pt))))
   (for i 0 (- (len pt) 1)
      (= op (string op (encode (string (pt i)) (string (k i))))))
   (formatstr op)))
    
(= decode-string (fn (ct k)
   (= ct (formatstr ct))
   (= k (formatstr k))
   (while (< (len k) (len ct))
      (for i 0 (- (len ct) 1)
   	(= k (string k (encode (string (k i)) (string (ct i)))))))
   (encode-string ct k)))

(decode-string "PNOBLWHXDI" "diana") ; => "hello world"

