(* Exercice 1 *)

let rec last_but_one = function
| a::[b] -> a
| a::b -> last_but_one b
| [] -> () ;;




(* Exercice 2 *)

let rec somme = function
| [] -> 0
| a::b -> a + somme b;;



let produit lst = List.fold_right (fun a b -> a * b) lst 1;;




(* Exercice 3 *)

let rec exist prop lst = match lst with 
  | [] -> false
  | a::q -> (prop a) || (exist prop q);;


let exist_2 prop lst = List.fold_right (fun a b -> (prop a) || b) lst false;;



let rec for_all prop lst = match lst with
  | [] -> true
  | a::q -> (prop a) && (for_all prop q);;


let for_all_2 prop lst = List.fold_right (fun a b -> (prop a) && b) lst true;;


(* Exercice 4 *)

let prefixes lst =
  let rec f lst ls_rev = match ls_rev with
    | [] -> lst
    | a::q -> f ((List.rev q)::lst) q
in f [lst] (List.rev lst);;




(* Exercice 5 *)

let rec n_prop lst prop n = match (List.length lst), n with
    | 0,_ -> failwith "error"
    | _,1 -> if (prop (List.hd lst)) then (List.hd lst) else (n_prop (List.tl lst) prop n)
    | _ -> if (prop (List.hd lst)) then (n_prop (List.tl lst) prop (n-1)) else (n_prop (List.tl lst) prop n);;


let last_prop lst prop =
  let rec f lst acc = match lst with 
  | [] -> acc
  | a::q -> if (prop a) then f q a else f q acc
in let a = f lst (List.hd lst) in if prop a then a else failwith "Error no element verify the property";;




(* Exercice 6 *)

let rec miroir = function
| [] -> []
| a::q -> (miroir q) @ [a];;


let miroir_2 lst = List.fold_right (fun a b -> b @ [a]) lst [];;


let miroir_lineaire lst =
  let rec f lst acc = match lst with
  | [] -> acc
  | h::q -> f q (h::acc)
in f lst [];;



(* Exercice 7 *)


let rotg lst = (List.tl lst) @ [List.hd lst];;


let rotd lst = 
  let list_but_not_last = ref [] in
  let last_but_not_list = (let rec f lst  = match lst with
                        | [a] -> a
                        | h::q -> list_but_not_last := h::(!list_but_not_last);
                                  f q
                        | [] -> List.hd lst
                      in f lst) in last_but_not_list::(List.rev !list_but_not_last);;





(* Exercice 8 *)

let rec delete n lst = match n,lst with
    | _,[] -> []
    | 1,(h::q) -> q
    | b,(h::q) -> h::(delete (n-1) q);;

let rec insert el n lst = match n,lst with
  | 1,ls -> el::ls
  | n,[] -> failwith "Liste trop courte"
  | n,h::q -> h::(insert el (n-1) q);;




(* Exercice 9 *)

(* type : ('a -> bool) -> 'a list -> 'a list *)


(* Prend en argument une propriété f et une liste de 'a. Renvoie l'ensemble des éléments de la liste de 'a qui vérifient f. *)




(* Exercice 10 *)

let rec purge = function
    | [] -> []
    | h::q when (List.mem h q) ->  purge q
    | h::q -> h::(purge q);;


let purge_2 lst =
  List.rev (let rec f lst acc = match lst with
    | [] -> acc
    | h::q when not (List.mem h acc) ->  f q (h::acc)
    | h::q -> f q acc
in f lst []);;



(* Exercice 11 *)
(* n1 = List.length l1 / n2 = List.length l2  *)

let rec intersection l1 l2 = match l1 with
  | [] -> []
  | h::q when List.mem h l2 -> h::(intersection q l2)
  | h::q -> intersection q l2;;

(* List.mem h l2 est en O(n2) on fait l'instruction n1 fois. On est en O(n1*n2) *)

let rec union l1 l2 = match l1 with
    | [] -> l2
    | h::q when List.mem h l2 -> union q l2
    | h::q -> h::(union q l2);;

(* De même, on est en O(n1*n2) *)


let diff_sym l1 l2 = 
  let c1 = (let rec f1 l1 l2 = match l1 with
  | [] ->[]
  | h::q when List.mem h l2 -> f1 q l2
  | h::q -> h::(f1 q l2)
  in f1 l1 l2)
  and c2 = (let rec f2 l1 l2 = match l2 with
  | [] -> []
  | h::q when List.mem h l1 -> f2 l1 q
  | h::q -> h::(f2 l1 q)
  in f2 l1 l2) in c1 @ c2;;

(* Pour le calcul de c1, on est en O(n1*n2), pour le calcul de c2 aussi. Finalement, avec 
la concaténation finale en au plus O(n1), On est en O(2*n1*n2 + n1) soit O(n1*n2) *)

let egal l1 l2 = 
  let c1 = (let rec f1 l1 l2 = match l1 with
  | [] -> true
  | h::q -> (List.mem h l2) && (f1 q l2)
        in f1 l1 l2) 
  and c2 = (let rec f2 l1 l2 = match l2 with
  | [] -> true
  | h::q -> (List.mem h l1) && (f2 l1 q)
in f2 l1 l2) in c1 && c2;;


let egal_2 l1 l2 = (diff_sym l1 l2 = []);;

(* Ici, c1 et c2 se calculent respectivement en au pire O(n1*n2) et O(n1*n2). Finalement, on est en O(n1*n2)   *)

