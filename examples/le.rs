// stone:job stone:math.le
// stone:function le_rs

#[no_mangle]
pub extern "C" fn le_rs(x: f64, y: f64) -> bool { x <= y }
