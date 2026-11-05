// stone:job stone:math.nonzero
// stone:function nonzero_rs

#[no_mangle]
pub extern "C" fn nonzero_rs(x: f64) -> bool { x != 0.0 }
