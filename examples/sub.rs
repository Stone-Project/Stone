// stone:job stone:math.sub
// stone:function sub_rs

#[no_mangle]
pub extern "C" fn sub_rs(x: f64, y: f64) -> f64 {
    x - y
}
