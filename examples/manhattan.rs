// stone:job stone:math.manhattan
// stone:function manhattan_rs

#[no_mangle]
pub extern "C" fn manhattan_rs(x1: f64, y1: f64, x2: f64, y2: f64) -> f64 { (x2-x1).abs() + (y2-y1).abs() }
