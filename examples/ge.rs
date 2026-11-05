// stone:job stone:math.ge
// stone:function ge_rs

#[no_mangle]
pub extern "C" fn ge_rs(x: f64, y: f64) -> bool { x >= y }
