(= curr-ymd (date))
(= curr-month (curr-ymd 1))
(= prev-month (fn (month) (if (< 0 (- month 1)) (- month 1) 12)))
(= next-month (fn (month) (if (> 13 (+ month 1)) (+ month 1) 1)))

(= month-names '(nil January February March April May June July
                     August September October November December))
(= month-lengths '(nil 31 28 31 30 31 30 31 31 30 31 30 31))
(= day-names '(Sunday Monday Tuesday Wednesday Thursday Friday Saturday))

(= get-month-name (fn (month) (month-names month)))
(= get-weekday-num (fn (year month day)
   (with (helper '(nil 3 2 5 0 3 5 1 4 6 2 4))
   (if (< month 3) (= year (- year 1)))
   (mod (+ year (helper (- month 1)) day
        (apply + (map [trunc (/ year _)] '(4 -100 400))))
   7))))
(= get-weekday-name (fn (year month day)
  (day-names (get-weekday-num year month day))))
(= leap? (fn (year)
  (if (and (is 0 (mod year 4)) (isnt 0 (mod year 100))) year
      (unless (< 0 (+ (mod year 100) (mod year 400))) year))))

(= print-days-list (fn (y m)
  (with (mname (month-names m)
  1st (get-weekday-num y m 1)
  end (get-weekday-num y (+ m 1) 0)
  mlen (if (and (is m 2) (leap? y)) 29 (month-lengths m)))
  (prs mname "begins on" (day-names 1st) "the 1st"
       "and ends on" (day-names end) mname mlen ".\n")
  (up d 1 mlen
      (prn (month-names m) " " d ": " (get-weekday-name y m d))))))

(print-days-list 2020 2)
