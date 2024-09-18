module TupleSet = Set.Make(struct
  type t = int * int
  let compare = compare
end)

let to_tup dir = let num = String.sub dir 1 (String.length dir - 1) |> int_of_string in
  let xy = match String.get dir 0 with
  | 'U' -> (0, 1) 
  | 'D' -> (0, -1)
  | 'R' -> (1, 0)
  | _ -> (-1, 0) in
  List.init num (fun _ -> xy)


let rec scan sx sy = function
  | [] -> [] 
  | (x, y) :: rest -> (sx+x, sy+y) :: scan (sx+x) (sy+y) rest


let read_line stdin = 
  input_line stdin |> String.split_on_char ',' |> List.concat_map to_tup |> scan 0 0 |> TupleSet.of_list
  

  (* List.iter (fun (a, b) -> Printf.printf("%d,%d -> ") a b) dirs *)

let () = 
  let d1 = read_line stdin in 
  let d2 = read_line stdin in 
  (* TupleSet.inter d1 d2 |> TupleSet.iter (fun (a,b) -> Printf.printf "%d,%d -> " a b); *)
  (* TupleSet.inter d1 d2 |> TupleSet.to_list |> List.map (fun (a,b) -> abs(a) + abs(b)) |> List.iter (fun b -> Printf.printf "%d -> " b); *)
  TupleSet.inter d1 d2 |> TupleSet.to_list |> List.map (fun (a,b) -> abs(a) + abs(b)) |> List.fold_left min max_int |> Printf.printf "%d\n";
  (* Printf.printf "\n%d\n" (TupleSet.to_list d1 |> List.length); *)
  (* Printf.printf "\n%d\n" (TupleSet.to_list d2 |> List.length); *)
  (* List.iter (fun (a, b) -> Printf.printf("%d,%d -> ") a b) d1; *)
  (* let shared = List.filter (fun x -> List.exists (fun a -> a == x) d1) d2 in *)
  (* let num = List.map (fun (a, b) -> a+b) shared |> List.fold_left max min_int in *)
  (* Printf.printf "%d " num; *)
