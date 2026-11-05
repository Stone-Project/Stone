// stone:job stone:math.gt
// stone:function gt_rs

#[no_mangle]
pub extern "C" fn gt_rs(x: f64, y: f64) -> bool { x > y }
