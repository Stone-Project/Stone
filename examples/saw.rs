// stone:job stone:math.saw
// stone:function saw_rs

#[no_mangle]
pub extern "C" fn saw_rs(x: f64) -> f64 { x.rem_euclid(1.0) }
