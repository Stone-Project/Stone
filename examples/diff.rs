// stone:job stone:math.diff
// stone:function diff_rs

#[no_mangle]
pub extern "C" fn diff_rs(x: f64, y: f64) -> f64 {
    if x >= y { x - y } else { y - x }
}
